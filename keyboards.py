from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.emoji import emojize


red_exclamation_mark = '\U00002757'
right_arrow = '\U000027A1'
left_arrow = '\U00002B05'
curving_arrow = '\U000021A9'
house = '\U0001F3E0'

def country_buttons(countries):
    country_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    i = 0
    
    if len(countries) % 2 == 1:
        btn = KeyboardButton(red_exclamation_mark + ' ' + countries[0])
        country_markup = country_markup.row(btn)

        i += 1
        
    while i < len(countries):
        btn_l = KeyboardButton(red_exclamation_mark + ' ' + countries[i])
        btn_r = KeyboardButton(red_exclamation_mark + ' ' + countries[i + 1])
        
        country_markup = country_markup.row(btn_l, btn_r)

        i += 2

    return country_markup

def next_prev_buttons(page, all_pages):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    if page > 1 and page < all_pages:
        markup = markup.row(KeyboardButton(left_arrow + ' Предыдущая'), KeyboardButton(right_arrow + ' Следующая'))

    elif page > 1:
        markup = markup.row(KeyboardButton(left_arrow + ' Предыдущая'))

    elif page < all_pages:
        markup = markup.row(KeyboardButton(right_arrow + ' Следующая'))

    markup = markup.row(KeyboardButton(curving_arrow + ' Выбрать страну'))

    return markup
        