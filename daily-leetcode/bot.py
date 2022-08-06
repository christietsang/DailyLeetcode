import slack_sdk as slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, request, Response
from slackeventsapi import SlackEventAdapter
from apscheduler.schedulers.background import BackgroundScheduler
import atexit
from problem_filter import choose_question
from category_compiler import compile_categories, compile_categories_and_count
# import res

current_attributes = {'current_difficulty': 'Easy',
                      'current_category': 'array'}

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(
    os.environ['SIGNIN_SECRET'], '/slack/events', app)

client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
BOT_ID = client.api_call("auth.test")['user_id']


@slack_event_adapter.on('message')
def message(payload):
    event = payload.get('event', {})
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')

    if BOT_ID != user_id:
        client.chat_postMessage(channel=channel_id, text=text)


@app.route('/difficulty', methods=['POST'])
def difficulty():
    data = request.form
    channel_id = data.get('channel_id')
    level = data.get("text")

    if level in ['Easy', 'Medium', 'Hard']:
        current_attributes["current_difficulty"] = level
        client.chat_postMessage(
            channel=channel_id, text=f"Category is now {level}")
    else:
        client.chat_postMessage(
            channel=channel_id, text=f"{level} is invalid.")
    return Response(), 200


@app.route('/category', methods=['POST'])
def category():
    data = request.form
    channel_id = data.get('channel_id')
    category = data.get("text")
    category_list = compile_categories()

    if category in category_list:
        current_attributes["current_category"] = category
        client.chat_postMessage(
            channel=channel_id, text=f"Category is now {category}")
    else:
        client.chat_postMessage(
            channel=channel_id, text=f"{category} is invalid. Type '/options' for valid categories")
    return Response(), 200


@app.route('/options', methods=['POST'])
def options():
    data = request.form
    channel_id = data.get('channel_id')
    message = ''
    for question, count in compile_categories_and_count():
        message += f"{question} ({count})\n"

    client.chat_postMessage(
        channel=channel_id, text=f"{message}")
    return Response(), 200


@app.route('/post-question', methods=['POST'])
def post_question():
    message = choose_question(current_attributes)
    client.chat_postMessage(channel=message['channel'], text=message['text'])
    slackBody = {
        "text": "Test"
    }
    Response.send(slackBody)


def scheduled():
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=post_question, trigger="interval", minutes=30)
    scheduler.start()
    atexit.register(lambda: scheduler.shutdown())


if __name__ == "__main__":
    scheduled()
    app.run(debug=True, use_reloader=False)
