# app.py
import os
import telebot
from dotenv import load_dotenv
load_dotenv()


token = os.getenv("BOT_TOKEN")
if not token:
    raise SystemExit("Set BOT_TOKEN in environment")

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start(m):
    bot.reply_to(m, "Здравствуйте. Наберите /help.")

@bot.message_handler(commands=["help"])
def help_(m):
    bot.reply_to(
        m,
        "/todo\n"
        "/weather <город>\n"
        "/rate <BASE> <SYM1,SYM2>\n"
        "/fileinfo\n"
        "/stats"
    )

if __name__ == "__main__":
    bot.infinity_polling(skip_pending=True)
