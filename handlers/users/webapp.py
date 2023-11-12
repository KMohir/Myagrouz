import time
from lxml import etree
from aiogram.dispatcher.filters import Command
import config
import logging
import openai
import asyncio
from gpytranslate import Translator
import json
import requests
from bs4 import BeautifulSoup
from aiogram import Bot, Dispatcher, executor, types
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ParseMode, Message, ReplyKeyboardRemove, ContentType
from aiogram.types.web_app_info import WebAppInfo
from db import db
from keyboards.default.reply import key, get_lang_for_button, change_lang, get_lang_for_buttonru
from keyboards.inline.support import langMenu, support_keyboard, yesno
from loader import dp, bot

# from keyboards.default.reply import get_lang_for_button, get_project_for_user
from states.state import answer, RegistrationStates, questions, language, imagestate
from translation import _
from utils.set_bot_commands import set_default_commands
import ast
import random
import time
from multiprocessing.pool import Pool

from aiogram import Bot, Dispatcher

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions

from selenium.webdriver.common.by import By
import time

from selenium.webdriver.chrome.service import Service
import ast
from aiogram import Bot, Dispatcher


from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.options import Options
@dp.message_handler(text="Orqaga")
@dp.message_handler(text="Назад")
async def back(message: types.Message):
    await message.answer("O'zingi kerakli bo'limni pasdan tanlap oling", reply_markup=get_lang_for_button())

@dp.message_handler(text="Agro expert")
@dp.message_handler(Command('about'))
async def image(message:Message,state: FSMContext):

    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Agro expert', web_app=WebAppInfo(
        url=str('https://assalomagro.uz'))))
    markup.add(types.KeyboardButton('Orqaga'))
    await bot.send_message(message.chat.id, 'AssalomAgro web sayti', reply_markup=markup)

@dp.message_handler(text="O'simlik kasalliklari")
async def image(message:Message,state: FSMContext):

    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton("O'simlik kasalliklari", web_app=WebAppInfo(
        url=str('https://old.assalomagro.uz/services/diseases'))))
    markup.add(types.KeyboardButton('Orqaga'))
    await bot.send_message(message.chat.id,  "O'simlik kasalliklari haqida pastgi tugmani bosip bilishingiz mumkun", reply_markup=markup)

@dp.message_handler(text="Zarakkunandalar")
async def image(message:Message,state: FSMContext):

    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Zarakkunandalar', web_app=WebAppInfo(
        url=str('https://old.assalomagro.uz/services/pests'))))
    markup.add(types.KeyboardButton('Orqaga'))
    await bot.send_message(message.chat.id,  "Zarakkunandalar haqida pastgi tugmani bosip bilishingiz mumkun", reply_markup=markup)

@dp.message_handler(text="Kimyoviy_vositalar")
async def image(message:Message,state: FSMContext):

    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Kimyoviy_vositalar', web_app=WebAppInfo(
        url=str('https://old.assalomagro.uz/services/chemical-products'))))
    markup.add(types.KeyboardButton('Orqaga'))
    await bot.send_message(message.chat.id,  "Kimyoviy_vositalar haqida pastgi tugmani bosip bilishingiz mumkun", reply_markup=markup)
@dp.message_handler(text="Begona_otlar")
async def image(message:Message,state: FSMContext):

    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Begona_otlar', web_app=WebAppInfo(
        url=str('https://old.assalomagro.uz/services/weeds'))))
    markup.add(types.KeyboardButton('Orqaga'))
    await bot.send_message(message.chat.id,  "Begona_otlar haqida pastgi tugmani bosip bilishingiz mumkun", reply_markup=markup)
