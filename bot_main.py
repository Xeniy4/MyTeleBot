from http.client import responses

import requests
from telebot import TeleBot, types
from urllib3 import request

from config import StandConfig
from telebot.types import Message
from models.bot_model import BotMessageResponse

config = StandConfig()
bot_token = config.bot_token
bot = TeleBot(token=bot_token)
"""Здесь будут функции, которые попробовать вызвать в командах в файле bot_command"""

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


def get_price_by_ticker(*, ticker: str) -> float:
    endpoint_binance = 'https://api.binance.com/api/v3/ticker/price'
    params = {'symbol':ticker}
    response = requests.get(endpoint_binance, params=params)
    data_response = response.json()
    price = round(data_response["price"], 2)
    return price


print("Пример работы с API Сервиса получения данных")
BASE_URL = 'http://www.cbr.ru/dataservice' #источник данных


# необходимо получить все параметры для основного запроса /data
# для этого последовательно получаем данные справочников

print("**** Список публикаций ****")
response = requests.get(f"{BASE_URL}/publications")
publication_object= response.json()
print(publication_object)

# bot.infinity_polling()  # запуск бота и прием сообщений
