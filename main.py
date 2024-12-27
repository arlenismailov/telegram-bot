import telebot
import requests
import json

bot = telebot.TeleBot('7675326861:AAGE-XW46hhotz0KqFBdVVBtcyotdMMUqyg')
API = 'da9abad7c2f64d0d90657e1d60ca6199'


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, рад тебя видеть! Hапиши название города')


import os


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]

        bot.reply_to(message, f'Сейчас погода: {temp}')

        # Абсолютный путь к изображению
        image = 'sun.png' if temp > 5.0 else 'cold.png'
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(BASE_DIR, image)

        try:
            with open(file_path, 'rb') as file:
                bot.send_photo(message.chat.id, file)
        except FileNotFoundError:
            bot.reply_to(message, "Не удалось найти изображение.")

    else:
        bot.reply_to(message, f'Город указан неверно')


bot.polling(none_stop=True)
