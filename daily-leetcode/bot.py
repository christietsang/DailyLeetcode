from cgitb import text
import slack_sdk as slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, request, Response
from slackeventsapi import SlackEventAdapter
from datetime import datetime, timedelta
import schedule

current_attributes = {'current_difficulty':'easy', 'current_category': ''} #to be filled later

scheduled_daily_problem = {'text': 'This is a placeholder for now', 'post_at':int((datetime.now() + timedelta(seconds=10)).timestamp()), 'channel':'C03S0RK0J8P'}

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(os.environ['SIGNIN_SECRET'],'/slack/events',app)

client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
BOT_ID = client.api_call("auth.test")['user_id']

@slack_event_adapter.on('message')
def message(payload):
    event = payload.get('event', {})
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')

    if BOT_ID != user_id:
        client.chat_postMessage(channel=channel_id, text = text)

@app.route('/difficulty', methods=['POST'])
def difficulty():
    data = request.form
    user_id = data.get('user')
    channel_id = data.get('channel_id')
    level = data.get('text')

    #Add validation here for levels, later
    client.chat_postMessage(channel = channel_id, text= f"Difficulty has been changed to {level}")
    return Response(), 200

def schedule_messages(messages):
    ids = []
    response = client.chat_scheduleMessage(
        channel=messages['channel'], text = messages['text'], post_at=messages['post_at'])
    id_ = response.get('id')
    ids.append(id_)
    return ids


if __name__ == "__main__":
    schedule_messages(scheduled_daily_problem)
    schedule.every().day.at("23:29").do()
    # schedule.run_pending()
    app.run(debug=True)
