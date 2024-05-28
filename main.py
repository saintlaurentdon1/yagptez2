from config import TELEGRAM_TOKEN
from aiogram import Bot, Dispatcher, types, executor
from neiro.text import get_response
from neiro.test import general_img
from neiro.smth import get_drafts

API_KEY='7337307051:AAEZcb44mof2TSvN6Uk_1KnWDsTF2Y3agIE'
bot = Bot(token=API_KEY)
dp = Dispatcher(bot)

async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command='/start', description= 'Команда запуска бота'),
        types.BotCommand(command='/get_drafts', description='Cгенерировать контрпик'),
        types.BotCommand(command='/general_img', description='Сгенерировать изображение'),
        types.BotCommand(command='/get_response', description='Cгенерировать промпт'),
    ]
    await bot.set_my_commands(commands)

@dp.message_handler(commands='start')
async def func_start(message: types.Message):
    await message.answer('Привет я твой нейросотрудник, который может помочь тебе с следующими задачами: Сгенерировать изображение(/general_img: название), '
                         'Придумать контрпик герою(/get_drafts: герой), сгенерировать промпт(/get_response: название)')


@dp.message_handler(commands='get_drafts')
async def get_dr(message: types.Message):
    text = message.get_args()
    response_dnd = await get_drafts(text)
    await message.answer(response_dnd)

@dp.message_handler(commands='general_img')
async def func_start(message: types.Message):
    text = message.get_args()
    response_img = await get_response(text)
    await message.reply('Идет генерация, подождите')
    try:
        image_data = general_img(response_img)
        await message.reply_photo(photo=image_data)
    except Exception as e:
        await message.reply(f'Произошла ошибка {e}')

@dp.message_handler(commands='get_response')
async def func_start(message: types.Message):
    text = message.get_args()
    response_text = await get_response(text)
    print(response_text)
    await message.reply(f"Промпт: {response_text}")

async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True, on_startup= on_startup)