from math import lgamma

from telebot import TeleBot
from config import StandConfig


config = StandConfig()
bot_token = config.bot_token
bot = TeleBot(token=bot_token)

# обработчик команд start и help с декоратором message_handler
@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    print(message)
    bot.reply_to(message, "обработчик команд start и help")


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    print(message)
    bot.reply_to(message, f"Hi, {message.chat.first_name}, your message= {message.text}"
                          f"your username = {message.chat.username}")



bot.infinity_polling()  # запуск бота и прием сообщений
# пока не работает из-за впн