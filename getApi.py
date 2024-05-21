import requests


import requests

# 假设有GPT-4.0模型的API URL
url = "https://api.openai.com/v1/engines/gpt-4.0/completions"

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1UaEVOVUpHTkVNMVFURTRNMEZCTWpkQ05UZzVNRFUxUlRVd1FVSkRNRU13UmtGRVFrRXpSZyJ9.eyJodHRwczovL2FwaS5vcGVuYWkuY29tL3Byb2ZpbGUiOnsiZW1haWwiOiI0NjM4ODI0MDhAcXEuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWV9LCJodHRwczovL2FwaS5vcGVuYWkuY29tL2F1dGgiOnsicG9pZCI6Im9yZy13S0x6SkNVSUR3MWFzcHhsUkZ5TUZoSHEiLCJ1c2VyX2lkIjoidXNlci1nSk85MHZYbnA2d3lPa0MzRlRBd1hyN20ifSwiaXNzIjoiaHR0cHM6Ly9hdXRoMC5vcGVuYWkuY29tLyIsInN1YiI6ImF1dGgwfDYzZjRjYjk4YjRiMWRmNTM2ZjNkZTU1NiIsImF1ZCI6WyJodHRwczovL2FwaS5vcGVuYWkuY29tL3YxIiwiaHR0cHM6Ly9vcGVuYWkub3BlbmFpLmF1dGgwYXBwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE3MDEwNjY1MjYsImV4cCI6MTcwMTkzMDUyNiwiYXpwIjoiVGRKSWNiZTE2V29USHROOTVueXl3aDVFNHlPbzZJdEciLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIG1vZGVsLnJlYWQgbW9kZWwucmVxdWVzdCBvcmdhbml6YXRpb24ucmVhZCBvcmdhbml6YXRpb24ud3JpdGUgb2ZmbGluZV9hY2Nlc3MifQ.vpI5P7yUXBKyabFmcY4gr0qlPwqT44PEXEs7gRmTgYNf7FV9rSpa4aJRR3i0wFRa5JLlgRU9SqHXNJDNlmROb90nGp2EPBeC9CD4iSu07KbdNHzHhi6xgog6-K0fIF6b0IXSEYuN57KIOioCya-aisd4jvcrhegwRx9daPRiW7T_l3569OhJoWp7hDPKoHuc1PqX7jFBBJ_ktS-NT4VKIj8Wpb2jtjEQvdG1dZhl-b7mXfWbZel2wb_chkrk7STzsW9N3aFMhswp5zyqOWRk30jX5sBrJwTmmuFbcCWcjK7AM4_9FTgcm6gk16vKE1FrmQDN8ej7ES0S9omixZ9LQQ'
}

data = {
    "model": "gpt-4.0",
    "prompt": "请解释什么是费马大定理",
    "max_tokens": 100
}

response = requests.post(url, headers=headers, json=data)

print("Status Code", response.status_code)
print("JSON Response ", response.json())


import openai
# url = "https://api.openai.com/v1/chat/completions"
# url = "https://openkey.cloud/v1/chat/completions"
#
# headers = {
#   'Content-Type': 'application/json',
#   # 填写OpenKEY生成的令牌/KEY，注意前面的 Bearer 要保留，并且和 KEY 中间有一个空格。
#   'Authorization': 'Bearer sk-870UOsDGMCto7e0JEUpeby54QtPbdIpCN6lKjZaqjNhmNO2p'
# }
#
# data = {
#   "model": "gpt-3.5-turbo",
#   "messages": [{"role": "user", "content": "请解释什么是费马大定理"}]
# }
#
# response = requests.post(url, headers=headers, json=data)
#
# print("Status Code", response.status_code)
# print("JSON Response ", response.json())
# def call_chatgpt_api(prompt, api_key):
#     url = "https://api.openai.com/v1/engines/davinci/completions"
#     headers = {
#         "Authorization": f"Bearer {api_key}"
#     }
#     data = {
#         "prompt": prompt,
#         "max_tokens": 150
#     }
#
#     response = requests.post(url, headers=headers, json=data)
#     response_json = response.json()
#
#     if response.status_code == 200:
#         return response_json["choices"][0]["text"].strip()
#     else:
#         return "Error: " + response_json.get("message", "Unknown error occurred")
#
# def main():
#     print("Welcome to ChatGPT!")
#     api_key = "sk-870UOsDGMCto7e0JEUpeby54QtPbdIpCN6lKjZaqjNhmNO2p"
#     prompts = ["Hello, ChatGPT!", "Tell me a joke.", "What's the weather like?"]
#
#     for prompt in prompts:
#         print(f"Sending prompt: '{prompt}'")
#         response = call_chatgpt_api(prompt, api_key)
#         print("Response from ChatGPT:", response)
#         print()
#
# if __name__ == "__main__":
#     main()
