import os
import telebot
from telebot import types

bot = telebot.TeleBot('7883182364:AAFZFk8yTdGw-p2IPzSFhBymiVrDQqXCjY4')

# Убедимся, что рабочая директория правильная
os.chdir(r'C:\Users\Arlen\django_lesson\telegram-bot\pythonProject')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Пeрeйти на сайт 😁')
    markup.row(btn1)
    btn2 = types.KeyboardButton('Удалить фото')
    btn3 = types.KeyboardButton('Изменить текст')
    markup.row(btn2, btn3)
    file = open('./img.png', 'rb')
    bot.send_photo(message.chat.id, file, reply_markup=markup)
    # bot.send_video(message.chat.id, file, reply_markup=markup)
    # bot.send_audio(message.chat.id, file, reply_markup=markup)

    bot.send_message(message.chat.id, 'hi', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)


def on_click(message):
    if message.text.lower() == 'Пeрeйти на сайт':
        bot.send_message(message.chat.id, 'Website is open')
    elif message.text == 'Удалить фото':
        bot.send_message(message.chat.id, 'Delete')


@bot.message_handler(content_types=['photo', 'video'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Пуруйти на сайт', url='https://www.youtube.com/watch?v=RpiWnPNTeww&t=42s')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Удалить фото', callback_data='delete')
    btn3 = types.InlineKeyboardButton('Изменить текст', callback_data='edit')
    markup.row(btn2, btn3)
    bot.reply_to(message, 'Какое красивое фото', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)


bot.polling(none_stop=True)
