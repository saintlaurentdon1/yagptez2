import time
import requests
import base64
from random import randint



def general_img(promt_text):
    promt = {
        "modelUri": "art://b1g3f13cj7d6d3ss2md9/yandex-art/latest",
        "generationOptions": {
            "seed": randint(1, 1000000)
        },
        "messages": [
            {
                "weight": 1,
                "text": promt_text
            }
        ]
    }

    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/imageGenerationAsync"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Api-Key AQVN0R4lEBG8YeN9fVqAJEXLmnPHGy9U8VrK57zN"
    }

    response = requests.post(url=url, headers=headers, json=promt)
    result = response.json()
    print(result)

    operator_id = result['id']

    operator_url = f"https://llm.api.cloud.yandex.net:443/operations/{operator_id}"

    while True:
        operator_response = requests.get(operator_url, headers=headers)
        operator_result = operator_response.json()
        if 'response' in operator_result:
            image_base54 = operator_result['response']['image']
            image_data = base64.b64decode(image_base54)
            return image_data
        else:
            time.sleep(5)
