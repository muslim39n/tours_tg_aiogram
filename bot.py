from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from aiogram.types import ParseMode

import requests

import config
import keyboards as kb
import botmessages

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_message_handler(message: types.Message):
    user_data = {}
    user_data['user_id'] = message.from_user['id']
    
    if 'username' in message.from_user:
        user_data['username'] = message.from_user['username']
    
    if 'first_name' in message.from_user:
        user_data['name'] = message.from_user['first_name']

    if 'last_name' in message.from_user:
        user_data['lastname'] = message.from_user['last_name']

    if 'phone_number' in message.from_user:
        user_data['phone_number'] = message.from_user['phone_number']

    res = requests.post(config.HOME_LINK + 'api/tg/new_tg_user/', data = user_data)

    print(res.text)

    res = requests.get(config.HOME_LINK + 'api/loc/countries/ru/')
    countries = [i['name_ru'] for i in res.json()]
    await bot.send_message(message.from_user.id, 'gg', reply_markup=kb.country_buttons(countries))


@dp.message_handler()
async def other_message_handler(message: types.Message):
    print(message)
    # IF COUNTRY
    if kb.red_exclamation_mark in message.text:
        
        words_list = message.text.split(' ')
        if len(words_list) != 2 or words_list[0] != kb.red_exclamation_mark:
            await bot.send_message(message.from_user.id, 'Ничего не найдено')
            return

        res = requests.get(f'{config.HOME_LINK}api/tour/from_almaty?country={words_list[1]}&user={message.from_user.id}')
        
        print(res.json())

        if res.status_code == 404:
            await bot.send_message(message.from_user.id, 'Ничего не найдено')
            return

        await bot.send_message(message.from_user.id, 
                            botmessages.tour_messages(res.json()), 
                            parse_mode=ParseMode.HTML, 
                            reply_markup=kb.next_prev_buttons(res.json()['page'], res.json()['all_pages']))

    elif message.text == kb.left_arrow + ' Предыдущая':
        res = requests.get(f'{config.HOME_LINK}api/tg/prev_next/prev?user={message.from_user.id}')
        
        if res.status_code == 404:
            await bot.send_message(message.from_user.id, 'Ничего не найдено')
            return
        await bot.send_message(message.from_user.id, 
                            botmessages.tour_messages(res.json()), 
                            parse_mode=ParseMode.HTML, 
                            reply_markup=kb.next_prev_buttons(res.json()['page'], res.json()['all_pages']))
        

    elif message.text == kb.right_arrow + ' Следующая':
        res = requests.get(f'{config.HOME_LINK}api/tg/prev_next/next?user={message.from_user.id}')
        if res.status_code == 404:
            await bot.send_message(message.from_user.id, 'Ничего не найдено')
            return
        await bot.send_message(message.from_user.id, 
                            botmessages.tour_messages(res.json()), 
                            parse_mode=ParseMode.HTML, 
                            reply_markup=kb.next_prev_buttons(res.json()['page'], res.json()['all_pages']))

if __name__ == '__main__':
    executor.start_polling(dp)