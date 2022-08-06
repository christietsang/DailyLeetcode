import http.client

def question_generator():
    conn = http.client.HTTPSConnection("leetcode.com")

    payload = "{\n  \"query\": \"\\n    query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {\\n  problemsetQuestionList: questionList(\\n    categorySlug: $categorySlug\\n    limit: $limit\\n    skip: $skip\\n    filters: $filters\\n  ) {\\n    total: totalNum\\n    questions: data {\\n      acRate\\n      difficulty\\n      freqBar\\n      frontendQuestionId: questionFrontendId\\n      isFavor\\n      paidOnly: isPaidOnly\\n      status\\n      title\\n      titleSlug\\n      topicTags {\\n        name\\n        id\\n        slug\\n      }\\n      hasSolution\\n      hasVideoSolution\\n    }\\n  }\\n}\\n    \",\n  \"variables\": {\n    \"categorySlug\": \"\",\n    \"skip\": 0,\n    \"limit\": 2300,\n    \"filters\": {}\n  }\n}"

    headers = {
        'cookie': "csrftoken=GDglrEY3SivNUcX2u6OvpREytGLP2khjm2kP087np4Mz6y1rBuRAYd2jAxRgDBGa; LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiMzg3NjUwNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYTQxOTVjOGI0NzZkMjc1NTA1MjgyZDEyM2U5NmZjYTI5MGZmOGI3NiIsImlkIjozODc2NTA1LCJlbWFpbCI6ImJlbGFsa0BsaXZlLmNhIiwidXNlcm5hbWUiOiJhc2xrMTIiLCJ1c2VyX3NsdWciOiJhc2xrMTIiLCJhdmF0YXIiOiJodHRwczovL3MzLXVzLXdlc3QtMS5hbWF6b25hd3MuY29tL3MzLWxjLXVwbG9hZC9hc3NldHMvZGVmYXVsdF9hdmF0YXIuanBnIiwicmVmcmVzaGVkX2F0IjoxNjU5NjUyNDMxLCJpcCI6IjcwLjc5LjIzNS4yMzYiLCJpZGVudGl0eSI6ImEwOTA5ODEwYTZkMTMyODMyZTI4ZWY2ZGExOGVjNzdjIiwic2Vzc2lvbl9pZCI6MjU1NzQwNjgsIl9zZXNzaW9uX2V4cGlyeSI6MTIwOTYwMH0.a6YQf2gN5LhQD9v0qkTesL5Oj8paVRvtNdBUfuF7CB0; NEW_PROBLEMLIST_PAGE=1",
        'authority': "leetcode.com",
        'accept': "*/*",
        'accept-language': "en-US,en;q=0.9,fr;q=0.8",
        'authorization': "",
        'content-type': "application/json",
        'dnt': "1",
        'origin': "https://leetcode.com",
        'referer': "https://leetcode.com/problemset/all/",
        'sec-ch-ua': "^\^Chromium^^;v=^\^104^^, ^\^"
        }

    conn.request("GET", "/graphql", payload, headers)

    res = conn.getresponse()
    data = res.read()

    return data.decode("utf-8")

def category_generator():
    conn = http.client.HTTPSConnection("leetcode.com")

    payload = ""

    headers = {
        'cookie': "csrftoken=GDglrEY3SivNUcX2u6OvpREytGLP2khjm2kP087np4Mz6y1rBuRAYd2jAxRgDBGa; messages=^\^f9ed3ac9e76330f7d160361672323611f6ca76f9^$^[^[^^^^__json_message^\^\^\^^^0540^^05425^^054^^^^Successfully signed in as aslk12.^\^\^\^^]^]^^; LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiMzg3NjUwNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYTQxOTVjOGI0NzZkMjc1NTA1MjgyZDEyM2U5NmZjYTI5MGZmOGI3NiIsImlkIjozODc2NTA1LCJlbWFpbCI6ImJlbGFsa0BsaXZlLmNhIiwidXNlcm5hbWUiOiJhc2xrMTIiLCJ1c2VyX3NsdWciOiJhc2xrMTIiLCJhdmF0YXIiOiJodHRwczovL3MzLXVzLXdlc3QtMS5hbWF6b25hd3MuY29tL3MzLWxjLXVwbG9hZC9hc3NldHMvZGVmYXVsdF9hdmF0YXIuanBnIiwicmVmcmVzaGVkX2F0IjoxNjU5NjUyNDMxLCJpcCI6IjcwLjc5LjIzNS4yMzYiLCJpZGVudGl0eSI6ImEwOTA5ODEwYTZkMTMyODMyZTI4ZWY2ZGExOGVjNzdjIiwic2Vzc2lvbl9pZCI6MjU1NzQwNjgsIl9zZXNzaW9uX2V4cGlyeSI6MTIwOTYwMH0.a6YQf2gN5LhQD9v0qkTesL5Oj8paVRvtNdBUfuF7CB0; NEW_PROBLEMLIST_PAGE=1",
        'authority': "leetcode.com",
        'accept': "*/*",
        'accept-language': "en-US,en;q=0.9,fr;q=0.8",
        'authorization': "",
        'content-type': "application/json",
        'dnt': "1",
        'origin': "https://leetcode.com",
        'referer': "https://leetcode.com/problemset/algorithms/",
        'sec-ch-ua': "^\^.Not/A",
        'sec-ch-ua-mobile': "?0",
        'sec-ch-ua-platform': "^\^Windows^^",
        'sec-fetch-dest': "empty",
        'sec-fetch-mode': "cors",
        'sec-fetch-site': "same-origin",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
        'x-csrftoken': "GDglrEY3SivNUcX2u6OvpREytGLP2khjm2kP087np4Mz6y1rBuRAYd2jAxRgDBGa"
        }

    conn.request("GET", "/_next/data/Ldb_Fcc-UKa_pLAqMwyAp/problem-list/top-interview-questions.json", payload, headers)

    res = conn.getresponse()
    data = res.read()

    return data.decode("utf-8")