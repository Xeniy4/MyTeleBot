from telebot import TeleBot, types
from config import StandConfig
from telebot.types import Message, ReplyKeyboardMarkup
import random

config = StandConfig()
bot_token = config.bot_token
bot = TeleBot(token=bot_token)

user_states = {}

compliments_girls = ["красивая", "умная", "добрая", "милая", "обаятельная", "очаровательная", "прелестная", "чудесная",
                     "замечательная", "восхитительная", "лучшая"]
compliments_boys = ["замечательный", "очаровательный", "восхитительный", "талантливый", "обаятельный", "душевный",
                    "светлый", "чуткий", "отзывчивый", "безупречный"]


@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    print(message)
    bot.reply_to(message, "обработчик команд start и help")


@bot.message_handler(commands=["comp"])
def send_compliment(message: Message):
    # Устанавливаем состояние: ждём выбора пола
    user_states[message.chat.id] = "awaiting_gender"
    # Создаём клавиатуру с кнопками
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    girl_button = types.KeyboardButton("girl")
    boy_button = types.KeyboardButton("boy")
    markup.add(girl_button, boy_button)

    # Отправляем сообщение с кнопками
    bot.send_message(
        message.chat.id,
        "You are boy or girl?",
        reply_markup=markup
    )


@bot.message_handler(func=lambda message: True)
def handle_gender_choice(message):
    chat_id = message.chat.id
    # Проверяем, находится ли пользователь в состоянии ожидания выбора пола
    if user_states.get(chat_id) == "awaiting_gender":
        if message.text == "girl":
            random_compliment = random.choice(compliments_girls)
        elif message.text == "boy":
            random_compliment = random.choice(compliments_boys)
        else:
            user_states[chat_id] = None
            return
        # Сбрасываем состояние после ответа
        user_states[chat_id] = None

        remove_markup = types.ReplyKeyboardRemove()
        bot.send_message(
            chat_id,
            random_compliment,
            reply_markup=remove_markup
        )
    else:
        # Если состояние не установлено, игнорируем сообщение
        pass


@bot.message_handler(commands=["help_holidays"])
def send_compliment(message: Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True,  one_time_keyboard=True)
    help_button = types.KeyboardButton("Да")
    cansel_button = types.KeyboardButton("Нет")
    markup.add(help_button, cansel_button)

    bot.send_message(
        message.chat.id,
        "Вы хотите следить за туром?",
        reply_markup=markup
    )





bot.infinity_polling()  # запуск бота и прием сообщений

