import requests


async def get_response(message_text):
    prompt = {
        "modelUri": "gpt://b1g3f13cj7d6d3ss2md9/yandexgpt-lite",
        "completionOptions": {
            "stream": False,
            "temperature": 0.3,
            "maxTokens": "2000"
        },
        "messages": [
            {
                "role": "system",
                "text": "Ты - нейронная сеть которая помогает улучшать промт. Ты получаешь сообщение от пользователя и улучшаешь промт дополняя её нужными данными для правильной выдачи текста"
            },
            {
                "role": "user",
                "text": message_text
            }
        ]
    }

    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Api-Key AQVNyXLGET5_qNDS-D1pcffPheqUicHAnm58mFLH"
    }

    response = requests.post(url, headers=headers, json=prompt)
    result = response.json()
    magic_pr = result['result']['alternatives'][0]['message']['text']
    return magic_pr
