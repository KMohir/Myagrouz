import os
import re
from email._header_value_parser import ContentType
from io import BytesIO

import openai
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ParseMode, Message, ReplyKeyboardRemove
from aiogram.types import InputFile


from db import db
from handlers.users.start import t
from keyboards.default.reply import key, get_lang_for_button, direction, region, gender, gmail, check
from keyboards.inline.support import langMenu, support_keyboard, generate_grades, get_grades, yesno
from loader import dp, bot


# from keyboards.default.reply import get_lang_for_button, get_project_for_user
from states.state import answer, questions, ariza, RegistrationStates
from translation import _

global lang
@dp.message_handler(text="Savol berish")
@dp.message_handler(text="Задать вопрос")
async def chat0(message:Message,state:FSMContext):
    lang = db.get_lang(message.from_user.id)
    await message.answer(_("Agro boyicha savollingizni toliq yuborsengez boladi", lang))
    await RegistrationStates.chatgptfull.set()
@dp.message_handler(state=RegistrationStates.chatgptfull)
async def chat(message:Message,state:FSMContext):
    lang = db.get_lang(message.from_user.id)
    model_engine = "text-davinci-003"
    max_tokens = 128  # default 1024
    prompt = await t.translate(message.text, targetlang="en")
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt.text,
        max_tokens=max_tokens,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    await message.answer(_("Assalomagro javobni izlamoqda ...", lang))
    translated_result = await t.translate(completion.choices[0].text, targetlang=str(lang))
    await message.answer(f'Savol: {message.text}\n\nJavob: {translated_result.text}')
    await message.answer(_("Savolingizga javob ola oldizmi", lang),reply_markup=yesno(message))
    await state.finish()
