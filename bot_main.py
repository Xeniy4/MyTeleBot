from telebot import TeleBot, types
from config import StandConfig
from telebot.types import Message
from models.bot_model import BotMessageResponse

config = StandConfig()
bot_token = config.bot_token
bot = TeleBot(token=bot_token)


# эхо любого сообщения
# @bot.message_handler(func=lambda message: True)
# def echo_message(message: Message) -> BotMessageResponse:
#     print(message)
#     response_text = (
#         f"Hi, {message.from_user.first_name}!\n"
#         f"Your message: {message.text}\n"
#         f"Your username: @{message.from_user.username if message.from_user.username else 'not set'}\n"
#         f"Your telegram_id: {message.from_user.id}\n"
#         f"{"You are bot" if message.from_user.is_bot else "You are not bot"}\n"
#         f"{"Your lastname:" if message.from_user.last_name else "You have not lastname"}\n"
#         f"{"Your title:" if message.chat.title else "You have not title"}"
#     )
#     bot.reply_to(message, response_text)
#     response_model = BotMessageResponse()
#     return response_model






# bot.infinity_polling()  # запуск бота и прием сообщений
