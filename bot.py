from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
import asyncio

# Replace with your bot token and web app URL
TOKEN = "7879598325:AAFRhrWVUanbI3gxEb4W6Bm1GroQTudgZUQ"
WEB_APP_URL = "https://yourusername.github.io/telegram-webapp/"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    web_button = InlineKeyboardButton(
        text="Launch Telegram Web",
        web_app=WebAppInfo(url=WEB_APP_URL)
    )
    keyboard.add(web_button)
    
    await message.answer("Click below to open Telegram Web:", reply_markup=keyboard)

async def main():
    await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(main())
