from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from db import db
from translation import _
import requests

def get_lang_for_button():

    button=ReplyKeyboardMarkup(

[
    [
        KeyboardButton(text="Agrometeo", web_app=WebAppInfo(
        url=str('https://lucky-sunshine-c34c2f.netlify.app'))),

    ],
    [
        KeyboardButton(text="Болезни растений", web_app=WebAppInfo(
        url=str('https://old.assalomagro.uz/ru/services/diseases'))),
        KeyboardButton(text="Вредители", web_app=WebAppInfo(
        url=str('https://old.assalomagro.uz/ru/services/pests')))
    ],
    [
        KeyboardButton(text="Химические средства", web_app=WebAppInfo(
        url=str('https://old.assalomagro.uz/ru/services/chemical-products'))),

    ],


    [
        KeyboardButton(text="Orqaga"),

    ]

        ],
        resize_keyboard=True
    )
    return button
