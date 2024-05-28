import requests
from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN

API_KEY='7337307051:AAEZcb44mof2TSvN6Uk_1KnWDsTF2Y3agIE'
bot = Bot(token=API_KEY)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: types.Message):
  await message.reply('Привет, я нейроконсультант, который может помочь тебе с контрпиками героев')

async def get_drafts(message_text):
  prompt = {
    "modelUri": "gpt://b1g3f13cj7d6d3ss2md9/yandexgpt-lite",
    "completionOptions": {
      "stream": False,
      "temperature": 0.5,
      "maxTokens": "2000"
    },
    "messages": [
      {
        "role": "system",
        "text": "Ты драфтер в Dota 2, тебе на вход будут подаваться герой и информация о нём."
        "Тебе нужно придумать несколько лучших героев, которых можно взять против этого героя, учитывая следующие критерии:"
        "1. Процент побед и статистика предложенных героев против указанного героя."
        "2. Не предлагай способности героев."
        "3. Предлагай не менее пяти героев."
        "Всю статистику бери с сайта https://dota2protracker.com/"
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
  dnd = result['result']['alternatives'][0]['message']['text']
  print(dnd)
  return dnd
