translations={

    'ru':{
        "Savolingizga javob ola oldizmi":"Смогли ли мы получить ответ на ваш вопрос",
        "Agro soxa bo`yicha savollingizni yuboring":"Отправьте свой вопрос по агро",
        "Tabriklaymiz, ro'yxatdan muvaffaqiyatli o'tdingiz! !🎉":"Поздравляем, регистрация прошла успешно! ! 🎉",
        "Yangi savol bermoqchi bolsangiz yozishingiz mumkun":"Вы можете задать новый вопрос",
        "Telefon raqam noto'g'ri kiritildi, iltimos telefon raqamni +998XXXXXXXX formatda kiriting yoki 'Kontakni yuborish' tugmasiga bosing":'Номер телефона вставлен неправильно, пожалуйста отправьте номер телефона в формате +998XXXXXXXXX или нажмите на кнопку "Отправить контакт"',
        "Savol bermoqchi bolsangiz yozishingiz mumkun":"Если хотите Вы можете написать задать вопрос",
        "Assalomagro javobni izlamoqda ...":"Assalomagro ищет ответ ...",
        "Tilni o'zgartirish":"Изменить язык",
        "Agro expert":"Agro expert",
        "Tabriklaymiz, ro'yxatdan muvaffaqiyatli o'tdingiz! 🎉":"Поздравляем, регистрация прошла успешно! 🎉",
        "Savol bermoqchi bo'lsangiz yozishingiz mumkun":"Вы можете написать, если хотите задать вопрос",
        "O'zingizga kerakli bo'limni tanlang":"Выберите раздел, который вам нужен",
        "Orqaga":"Назад",
        "AssalomAgro web sayt":"Веб сайт AssalomAgro",
        "Zarakkunandalar":"Вредители",
        "Kimyoviy_vositalar":"Химические средства",
        "Begona_o'tlar":"Сорняки",
        "O'simlik kasalliklari":"Болезни растений",
        "E'lon joylash":"Размещение объявления",
        "E'lon joylasj uchun pastdagi tugmani bosing":"Нажмите кнопку ниже, чтобы разместить объявление",
        "O'zingizga kerakli bo'limni bo'limni tanlap oling":"Выберите раздел, который вам нужен",



        
    }

}

def _(text,lang='uz'):
    if lang=='uz':
        return text
    else:
        try:
            return translations[lang][text]
        except:
            return text