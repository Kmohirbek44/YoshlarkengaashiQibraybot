import requests
from aiogram import executor
from handlers import dp
import config
from items import item
async def on(dp):
    await item.set(dp)
    requests.post(f"https://api.telegram.org/bot{config.token}/sendMessage?chat_id=572054993&text='Online'")
    requests.post(f"https://api.telegram.org/bot{config.token}/sendMessage?chat_id=452785654&text='Online'")
executor.start_polling(dp,on_startup=on)

