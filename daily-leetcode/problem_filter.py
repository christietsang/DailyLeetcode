import json
from random import randrange
from leetcode_scraper import question_generator


def generate_channel_id():
    return "C03S9AM62SE"


def get_data():
    string_data = question_generator()
    data = json.loads(string_data)
    return data


def filter_questions(difficulty, category):
    data = get_data()
    all_problems = []
    for problem in data["data"]["problemsetQuestionList"]["questions"]:

        if not problem["paidOnly"] and problem["difficulty"] == difficulty and category in [tag_name for tag_name in [tag['slug'] for tag in problem['topicTags']]]:
            single_problem = problem["titleSlug"]
            all_problems.append(single_problem)

    return all_problems


def choose_question(attributes: dict) -> str:
    all_problems = filter_questions(
        difficulty=attributes['current_difficulty'], category=attributes['current_category'])
    if not all_problems:
        return {"text": f"No questions found with:\n*Difficulty*: {attributes['current_difficulty']}\n*Category*: {attributes['current_category']} :confused_dog:"}
    slug = all_problems[randrange(len(all_problems))]  # choose random problem
    title = slug.replace("-", " ")

    return {"text": f"*Today's Problem:* {title.title()}\n*Difficulty*: {attributes['current_difficulty']}\n*Category*: {(attributes['current_category']).title()}\n >Post your answers below and mark them with a `/spoiler` tag.\n >https://leetcode.com/problems/{slug}"}
