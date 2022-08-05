import requests
import json
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import schedule
import time
from random import randrange
from generator import json_generator

def post_problem(all_problems):
    slug = all_problems[randrange(len(all_problems))]  # choose random problem
    webhook_url = 'https://hooks.slack.com/services/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'
    output = { "text": "This week's warm-up problem: " + "https://leetcode.com/problems/" + slug }
    # post
    slack_response = requests.post(
        webhook_url, data=json.dumps(output),
        headers={'Content-Type': 'application/json'}
    )
    if slack_response.status_code != 200:
        raise ValueError(
            'Request to slack returned an error %s, the response is:\n%s'
            % (slack_response.status_code, slack_response.text)
        )

# get data
string_data = json_generator()
data = json.loads(string_data)

with open('ten_results.json', 'w') as file:
    file.write(f"{data}")

# filter-out premium ones, get slugs
all_problems = []
for problem in range(len(data["data"]["problemsetQuestionList"]["questions"])):
    if not data["data"]["problemsetQuestionList"]["questions"][0]["paidOnly"]:
        single_problem = data["data"]["problemsetQuestionList"]["questions"][0]["titleSlug"]
        all_problems.append(single_problem)


# schedule job
schedule.every().day.at("08:30").do(post_problem, all_problems)

while True:
    schedule.run_pending()
    time.sleep(1)
# post_problem(all_problems)  