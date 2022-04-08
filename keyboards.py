from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.emoji import emojize

def country_buttons(countries):
    country_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    i = 0

    if len(countries) % 2 == 1:
        btn = KeyboardButton(countries[0])
        country_markup = country_markup.row(btn)

        i += 1
        
    while i < len(countries):
        btn_l = KeyboardButton(countries[i])
        btn_r = KeyboardButton(countries[i + 1])
        
        country_markup = country_markup.row(btn_l, btn_r)

        i += 2

    return country_markup
