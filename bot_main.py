from telebot import TeleBot
from config import StandConfig


config = StandConfig()
bot_token = config.bot_token
bot = TeleBot(token=bot_token)

# обработчик команд start и help с декоратором message_handler
@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    print(message)
    bot.reply_to(message, "Answer")

bot.infinity_polling()  # запуск бота и прием сообщений
# пока не работает из-за впн