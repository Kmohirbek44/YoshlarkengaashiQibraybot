from geopy.geocoders import Nominatim
from aiogram import types
from items.calc_distance import choose_shortest
from items.callback import bobcallback
from keybord import locations_buttons,default
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, CallbackQuery

from keybord.Boblar import inline_kb1
from loader import dp, bot
from config import admins

@dp.message_handler(Command("start"))
async def start_bot(message:Message):
    await message.answer(f"Assalomu Alaykum va rahmatullohi va barakatuh {message.from_user.full_name}.\n"
                         f"pastigi tugmani bosing",
                         reply_markup=locations_buttons.keyboardstart
                         )
<<<<<<< HEAD
    for admin in admins:
        await bot.send_message(chat_id=admin,text=f"ismi_familiya:{message.from_user.full_name} id : {message.from_user.url}" )
=======
    # await bot.send_message(chat_id=572054993,text=f"ismi_familiya:{message.from_user.full_name} id : {message.from_user.url}" )
    await bot.send_message(chat_id=452785654,
                           text=f"ismi_familiya:{message.from_user.full_name} id : {message.from_user.url}")
>>>>>>> 336cbcc (fix bugs)
@dp.message_handler(text="Qibray_hokimiyatigacha_masofa")
async def show_on_map(message:Message):
    await bot.send_photo(chat_id=message.chat.id,photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR2i4PfxL2A9HPAYNPKdsZh-BMAdp_C3isQsA&usqp=CAU")
    await message.answer(f"Bu qismda siz turgan joydan Qibray hokimiyatigacha bo'lgan masofani ko'rishingiz mumkin Tepadagi rasmda qanday o'chanishi ko'rsatilgan\n"
                         f"Locatsiyangizni pastigi tugmani bosip tashlang",
                         reply_markup=locations_buttons.keyboard
                         )

<<<<<<< HEAD
@dp.message_handler(content_types=types.ContentTypes.LOCATION)
async def location(message:Message):
    global choose
    location1=message.location

    geolocator = Nominatim(user_agent="komilovmohirbekfda1@gmail.com")
    lat=location1.latitude
    lon=location1.longitude
    for admin in admins:
        bot.send_location(chat_id=admin,longitude=lon,latitude=lat)
    locationadress = geolocator.reverse(f"{lat} , {lon}")
    for admin in admins:

        await bot.send_message(chat_id=admin,text=f"{message.from_user.full_name} useri \n {locationadress} da")

    choose=choose_shortest(location1)
    await message.answer('Masofani bilish uchun pastagi tugmani bosing',reply_markup=default.button)
=======
    @dp.message_handler(content_types=types.ContentTypes.LOCATION)
    async def location(message:Message):
        global choose
        location1=message.location
        geolocator = Nominatim(user_agent="komilovmohirbekfda1@gmail.com")
        lat=location1.latitude
        lon=location1.longitude

        locationadress = geolocator.reverse(f"{lat} , {lon}")
        # await bot.send_message(chat_id=572054993,text=f"{message.from_user.full_name} useri\n {locationadress} yerda")
        await bot.send_message(chat_id=452785654, text=f"{message.from_user.full_name} useri\n {locationadress} yerda")
        choose=choose_shortest(location1)
        await message.answer('Masofani bilish uchun pastagi tugmani bosing',reply_markup=default.button)
>>>>>>> 336cbcc (fix bugs)

@dp.message_handler(text='Masofa')
async def Masofa(message: Message):
    c5 = choose
    text_format = "{shop_name}. gacha masofa {distance} km\n<a href='{url}'>Google</a>\n"
    text = "\n\n".join(
        [
            text_format.format(shop_name=shop_name, url=url, distance=distance)
            for shop_name, distance, url, shop_location in c5

        ]
    )
    await message.answer(f'{text} ', disable_web_page_preview=True, reply_markup=locations_buttons.keyboardstart)

