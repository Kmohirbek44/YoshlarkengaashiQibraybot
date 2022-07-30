from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard=ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text="location",
                       request_location=True

                       )
        ],

    ],
    resize_keyboard=True
)

keyboardstart=ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text="Qibray_hokimiyatigacha_masofa",

                       )
        ],
[
        KeyboardButton(text="Qonun_bo'yicha_ma'lumotlar",

                       )
        ],


    ],
    resize_keyboard=True
)
