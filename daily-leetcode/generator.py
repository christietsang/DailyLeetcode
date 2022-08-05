import http.client

def json_generator():
    conn = http.client.HTTPSConnection("leetcode.com")

    payload = "{\n  \"query\": \"\\n    query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {\\n  problemsetQuestionList: questionList(\\n    categorySlug: $categorySlug\\n    limit: $limit\\n    skip: $skip\\n    filters: $filters\\n  ) {\\n    total: totalNum\\n    questions: data {\\n      acRate\\n      difficulty\\n      freqBar\\n      frontendQuestionId: questionFrontendId\\n      isFavor\\n      paidOnly: isPaidOnly\\n      status\\n      title\\n      titleSlug\\n      topicTags {\\n        name\\n        id\\n        slug\\n      }\\n      hasSolution\\n      hasVideoSolution\\n    }\\n  }\\n}\\n    \",\n  \"variables\": {\n    \"categorySlug\": \"\",\n    \"skip\": 0,\n    \"limit\": 10,\n    \"filters\": {}\n  }\n}"

    headers = {
        'cookie': "_ga=GA1.2.70028370.1659649201; _gid=GA1.2.208480645.1659649201; gr_user_id=8ad98ddc-b049-4ade-9cef-63547f03042d; csrftoken=ZsewkXquQlIHc7O2peIGbIgH1Ih79ghMtzQiEpeDOLf0c3douE0xYpLYd10HE09d; messages=^\^e3a03d1a5568ed6c1b98bd59d4409bd9a67bb3c7^$^[^[^^^^__json_message^\^\^\^^^0540^^05425^^054^^^^Successfully signed in as user1419TO.^\^\^\^^]^]^^; LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiNTg0NTkyMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImFsbGF1dGguYWNjb3VudC5hdXRoX2JhY2tlbmRzLkF1dGhlbnRpY2F0aW9uQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjVhMGZiZmVjZTA4MGM1N2Q3MDc4YzI4YWRkMTRmMTQwZTA2Yzg3NGQiLCJpZCI6NTg0NTkyMSwiZW1haWwiOiJjaHJpc3RpZS50c2FuZzE5NUBnbWFpbC5jb20iLCJ1c2VybmFtZSI6InVzZXIxNDE5VE8iLCJ1c2VyX3NsdWciOiJ1c2VyMTQxOVRPIiwiYXZhdGFyIjoiaHR0cHM6Ly9hc3NldHMubGVldGNvZGUuY29tL3VzZXJzL2F2YXRhcnMvYXZhdGFyXzE2NDU1MDg4NTIucG5nIiwicmVmcmVzaGVkX2F0IjoxNjU5NjQ5MjI0LCJpcCI6IjcwLjc5LjIzNS4yMzYiLCJpZGVudGl0eSI6ImEwOTA5ODEwYTZkMTMyODMyZTI4ZWY2ZGExOGVjNzdjIiwic2Vzc2lvbl9pZCI6MjU1NzI5MDZ9.7davPGXbyivYt89_DmiKsPl9j-rAAfFj8yUm-9qjpUQ; 87b5a3c3f1a55520_gr_last_sent_cs1=user1419TO; NEW_PROBLEMLIST_PAGE=1; 87b5a3c3f1a55520_gr_session_id=b6c66f6c-b14a-4ab8-98a0-a6d385d22a00; 87b5a3c3f1a55520_gr_last_sent_sid_with_cs1=b6c66f6c-b14a-4ab8-98a0-a6d385d22a00; 87b5a3c3f1a55520_gr_session_id_b6c66f6c-b14a-4ab8-98a0-a6d385d22a00=true; __stripe_mid=4670c41b-7e15-40e8-b5de-48c8d1563626509bdb; c_a_u=^\^dXNlcjE0MTlUTw==:1oJn3K:_tl88KreRutnsgDPmZC79gEK3ME^^; _gat=1; 87b5a3c3f1a55520_gr_cs1=user1419TO",
        'authority': "leetcode.com",
        'accept': "*/*",
        'accept-language': "en-US,en;q=0.9",
        'authorization': "",
        'content-type': "application/json",
        'dnt': "1",
        'origin': "https://leetcode.com",
        'referer': "https://leetcode.com/problemset/all/",
        'sec-ch-ua': "^\^.Not/A",
        'sec-ch-ua-mobile': "?1",
        'sec-ch-ua-platform': "^\^Android^^",
        'sec-fetch-dest': "empty",
        'sec-fetch-mode': "cors",
        'sec-fetch-site': "same-origin",
        'user-agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
        'x-csrftoken': "ZsewkXquQlIHc7O2peIGbIgH1Ih79ghMtzQiEpeDOLf0c3douE0xYpLYd10HE09d"
        }

    conn.request("POST", "/graphql", payload, headers)

    res = conn.getresponse()
    data = res.read()

    return data.decode("utf-8")