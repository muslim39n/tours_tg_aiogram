from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import requests

import config
import keyboards as kb

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_message_handler(message: types.Message):
    response = requests.get(config.HOME_LINK + 'api/loc/countries/ru/')
    countries = [i['name_ru'] for i in response.json()]
    
    await bot.send_message(message.from_user.id, 'gg', reply_markup=kb.country_buttons(countries))


@dp.message_handler()
async def other_message_handler(message: types.Message):
    print(message)

    await bot.send_message(message.from_user.id, 'ok')

if __name__ == '__main__':
    executor.start_polling(dp)