# -*- coding: utf-8 -*-
import time

import openai
from lxml import etree
from aiogram.dispatcher.filters import Command
import config
import logging

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


from keyboards.default.reply import  get_lang_for_button
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
import g4f
# options = Options()
#
#
# # disable webdriver mode
#
# # for older ChromeDriver under version 79.0.3945.16
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option("useAutomationExtension", False)
#
# # for ChromeDriver version 79.0.3945.16 or over
# options.add_argument("--disable-blink-features=AutomationControlled")
#
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.9999.999 Safari/537.36"
#
#
#
#
# options.add_argument('headless')
# options.add_argument('window-size=1920x1080')
# options.add_argument("disable-gpu")
#
# driver = webdriver.Chrome(options=options)
#
#
#
#
#
#
#
#
# driver.get('https://www.picturethisai.com/ru/mobileSearch')
#
# photo1 = WebDriverWait(driver, 70).until(
#      EC.presence_of_element_located((By.XPATH, '//*[@id="mobile_vector_btn"]'))).click()
# apple = WebDriverWait(driver, 70).until(
#      EC.presence_of_element_located((By.XPATH, '//*[@id="appleid-signin"]/div/div[1]'))).click()
#
# time.sleep(5)
#
# all_windows = driver.window_handles
# driver.switch_to.window(all_windows[-1])
#
#
# apple_id_field = driver.find_element(By.XPATH,'//*[@id="account_name_text_field"]')
#
#
# apple_id_field.send_keys(str(input('email kiriting: ')))
# apple_id_field_next = driver.find_element(By.XPATH,'//*[@id="sign-in"]')
# apple_id_field_next.click()
# time.sleep(10)
# password_field = driver.find_element(By.XPATH, '//*[@id="password_text_field"]')  # Replace with the actual ID of the password input field.
#   # Replace with the actual ID of the password input field.
#
# password_field.send_keys('201219Fda1*')
# password_field = driver.find_element(By.XPATH, '//*[@id="sign-in"]').click()
# time.sleep(15)
#
# code1 = driver.find_element(By.XPATH, '//*[@id="char0"]')
# code1.send_keys(int(input('birinchi raqam: ')))
# code2 = driver.find_element(By.XPATH, '//*[@id="char1"]')
# code2.send_keys(int(input('ikkinchi raqam: ')))
# code3 = driver.find_element(By.XPATH, '//*[@id="char2"]')
# code3.send_keys(int(input('uchinchi raqam: ')))
# code4 = driver.find_element(By.XPATH, '//*[@id="char3"]')
# code4.send_keys(int(input('tortinchi raqam: ')))
# code5 = driver.find_element(By.XPATH, '//*[@id="char4"]')
# code5.send_keys(int(input('beshinchi raqam: ')))
# code6 = driver.find_element(By.XPATH, '//*[@id="char5"]')
# code6.send_keys(int(input('oltinchi raqam: ')))
#
#
#
# apple = WebDriverWait(driver, 70).until(
#      EC.presence_of_element_located((By.CLASS_NAME, 'float-left'))).click()
# apple = WebDriverWait(driver, 70).until(
#      EC.presence_of_element_located((By.CLASS_NAME, 'weight-medium'))).click()
#
#
# # You may need to locate the "Next" button and click it to complete the login process.
#
# print('Rasm tashash mumkun')
# driver.switch_to.window(all_windows[0])



@dp.message_handler(CommandStart())
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer("Agrometeo haqida bilmoqchi bo'lsangiz pastgi tugmani bosing", reply_markup=get_lang_for_button())





@dp.message_handler(text="Orqaga")
@dp.message_handler(text="Назад")
async def back(message: types.Message):

        await message.answer("Agrometeo haqida bilmoqchi bo'lsangiz pastgi tugmani bosing", reply_markup=get_lang_for_button())



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
