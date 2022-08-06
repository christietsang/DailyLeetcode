import json
from leetcode_scraper import category_generator



def get_data():
    string_data = category_generator()
    data = json.loads(string_data)
    return data


def compile_categories():
    categories = get_data()["pageProps"]["dehydratedState"]["queries"][0]["state"]["data"]
    return [category['slug'] for category in categories]

    
def compile_categories_and_count():
    categories = get_data()["pageProps"]["dehydratedState"]["queries"][0]["state"]["data"]
    categories.sort(key=lambda category: category['slug'])
    return [(category['slug'], category['questionCount']) for category in categories]