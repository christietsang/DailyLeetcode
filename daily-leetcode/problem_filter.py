import json
from random import randrange
from leetcode_scraper import question_generator


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
        return {"text": f"No questions found with:\nDifficulty: {attributes['current_difficulty']}\nCategory: {attributes['current_category']}", 'channel': 'C03S0RK0J8P'}
    slug = all_problems[randrange(len(all_problems))]  # choose random problem

    return {"text": f"Today's problem is {attributes['current_difficulty']} and is categorized as a {attributes['current_category']} question.\nPost your answers below, but mark them using the spoiler tag.\n https://leetcode.com/problems/{slug}", 'channel': 'C03S0RK0J8P'}
