import slack_sdk as slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, request, Response
from slackeventsapi import SlackEventAdapter
from apscheduler.schedulers.background import BackgroundScheduler
import atexit
from problem_filter import choose_question, generate_channel_id
from category_compiler import compile_categories, compile_categories_and_count

current_attributes = {'current_difficulty': 'Easy',
                      'current_category': 'array'}


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(
    os.environ['SIGNIN_SECRET'], '/slack/events', app)

client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
BOT_ID = client.api_call("auth.test")['user_id']


@app.route('/difficulty', methods=['POST'])
def difficulty():
    data = request.form
    level = data.get("text")

    if level in ['Easy', 'Medium', 'Hard']:
        current_attributes["current_difficulty"] = level
        client.chat_postMessage(
            channel=generate_channel_id(), text=f"Level is now *{level}* :cool-doge:")
    else:
        client.chat_postMessage(
            channel=generate_channel_id(), text=f"{level} is invalid. :sadpepe:")

    return Response(), 200


@app.route('/category', methods=['POST'])
def category():
    data = request.form
    category = data.get("text")
    category_list = compile_categories()

    if category in category_list:
        current_attributes["current_category"] = category
        client.chat_postMessage(
            channel=generate_channel_id(), text=f"Category is now *{category}* :conga_parrot:")
    else:
        client.chat_postMessage(
            channel=generate_channel_id(), text=f"{category} is invalid. :blob_help: Try `/options` for valid categories")
    return Response(), 200


@app.route('/options', methods=['POST'])
def options():
    message = ''
    for question, count in compile_categories_and_count():
        message += f">`{question}` ({count})\n"

    client.chat_postMessage(
        channel=generate_channel_id(), text=f"Your options are:\n{message} :catjam:")

    return Response(), 200


@app.route('/post-question', methods=['POST'])
def schedule_question():
    scheduler = BackgroundScheduler()
    scheduler.add_job(question_generator)
    scheduler.start()
    return Response(), 200


def question_generator():
    message = choose_question(current_attributes)
    client.chat_postMessage(
        channel=generate_channel_id(), text=message['text'])


def scheduled():
    scheduler = BackgroundScheduler()
    scheduler.add_job(schedule_question, 'cron',
                      day_of_week='mon-sun', hour=12, minute=00)
    scheduler.start()
    atexit.register(lambda: scheduler.shutdown())


if __name__ == "__main__":
    scheduled()
    app.run(debug=True, use_reloader=False)
