from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from items.callback import bobcallback


inline_kb1 = InlineKeyboardMarkup(row_width=2,
                                  inline_keyboard=[[
                                      InlineKeyboardButton(
                                          text='YOSHLAR MUAMMOLARINI O‘RGANISH VA HAL ETISH TIZIMINI YANADA '
                                               'TAKOMILLASHTIRISH CHORA-TADBIRLARI TO‘G‘RISIDA',
                                          callback_data=bobcallback.new(number="yoshlar")),
                                  ],
                                  [
                                      InlineKeyboardButton(text='1-bob. Umumiy qoidalar!',
                                                           callback_data=bobcallback.new(number="Umumiy qoidalar"))

                                  ],
                                      [
                                    InlineKeyboardButton(text='2-bob.  “Yoshlar daftari” jamg‘armalari mablag‘larini shakllantirish',
                                  callback_data=bobcallback.new(number="laridan"))],
                                      [
InlineKeyboardButton(text='3-bob.“Yoshlar daftari”  mablag‘laridan foydalanish',
                                                        callback_data=bobcallback.new(number="mablag"))

                                  ],
                                      [InlineKeyboardButton(text='4-bob. “Yoshlar daftari” jamg‘armalari  hisob va hisobot',
                                                        callback_data=bobcallback.new(number="hisob"))],
                                      [InlineKeyboardButton(text='5-bob. Yakunlovchi qoidalar',
                                                            callback_data=bobcallback.new(number="qoidalar")),
                                      ],
                                         [InlineKeyboardButton(text='Qoraqalpog‘iston Respublikasi, viloyatlar va Toshkent shahridagi “Yoshlar daftari” jamg‘armasi vasiylik kengashining NAMUNAVIY TARKIBI',
                                                            callback_data=bobcallback.new(number="namunaviy")),


                                      ],

                                    [InlineKeyboardButton(text='“Tuman (shahar)lardagi “Yoshlar daftari” jamg‘armasi vasiylik kengashining NAMUNAVIY TARKIBI',
                                                            callback_data=bobcallback.new(number="vasiylik")),
                                      ],
[InlineKeyboardButton(text='““Yoshlar daftari”ni yuritish orqali yoshlar muammolarini tizimli ravishda hal etish va ularni ijtimoiy qo‘llab-quvvatlash tartibi to‘g‘risida',
                                                            callback_data=bobcallback.new(number="mavzu")),
                                      ],
                                      [InlineKeyboardButton(text='1-bob. Umumiy qoidalar',
                                                            callback_data=bobcallback.new(number="1_2 bob")),
                                      ],
                                      [InlineKeyboardButton(text='2-bob. “Yoshlar daftari”ni shakllantirish',
                                                            callback_data=bobcallback.new(number="shakllantirish")),
                                      ],[InlineKeyboardButton(text='3-bob. “Yoshlar daftari” jamg‘armalari mablag‘laridan foydalanish',
                                                            callback_data=bobcallback.new(number="uchikki")),
                                      ],
                                      [InlineKeyboardButton(text='4-bob. Yordam turlarini berish tartibi',
                                                            callback_data=bobcallback.new(number="tort")),
                                      ],
                                      [InlineKeyboardButton(text='5-bob. “Yoshlar daftari”dan chiqarish tartibi',
                                                            callback_data=bobcallback.new(number="besh")),
                                      ],
                                      [InlineKeyboardButton(text='6-bob. Yakunlovchi qoidalar',
                                                            callback_data=bobcallback.new(number="olti"))]

                                  ])