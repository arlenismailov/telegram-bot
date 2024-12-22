import os
import telebot
from telebot import types

# Создание объекта бота с токеном для Telegram
bot = telebot.TeleBot('7883182364:AAFZFk8yTdGw-p2IPzSFhBymiVrDQqXCjY4')

# Убедимся, что рабочая директория соответствует местоположению проекта
os.chdir(r'C:\Users\Arlen\django_lesson\telegram-bot\pythonProject')


# Обработчик команды '/start'
@bot.message_handler(commands=['start'])
def start(message):
    # Создание клавиатуры с кнопками
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Пeрeйти на сайт 😁')  # Кнопка для перехода на сайт
    markup.row(btn1)
    btn2 = types.KeyboardButton('Удалить фото')  # Кнопка для удаления фото
    btn3 = types.KeyboardButton('Изменить текст')  # Кнопка для изменения текста
    markup.row(btn2, btn3)

    # Открытие файла с изображением
    file = open('./img.png', 'rb')
    # Отправка изображения пользователю
    bot.send_photo(message.chat.id, file, reply_markup=markup)

    # Отправка текстового сообщения с клавиатурой
    bot.send_message(message.chat.id, 'hi', reply_markup=markup)
    # Регистрация следующего действия пользователя
    bot.register_next_step_handler(message, on_click)


# Функция для обработки следующего действия пользователя
def on_click(message):
    if message.text.lower() == 'пeрeйти на сайт':
        bot.send_message(message.chat.id, 'Website is open')  # Сообщение при переходе на сайт
    elif message.text == 'Удалить фото':
        bot.send_message(message.chat.id, 'Delete')  # Сообщение при удалении фото


# Обработчик сообщений с фото или видео
@bot.message_handler(content_types=['photo', 'video'])
def get_photo(message):
    # Создание встроенной клавиатуры
    markup = types.InlineKeyboardMarkup()
    # Кнопка для перехода на сайт
    btn1 = types.InlineKeyboardButton('Пуруйти на сайт', url='https://www.youtube.com/watch?v=RpiWnPNTeww&t=42s')
    markup.row(btn1)
    # Кнопка для удаления фото
    btn2 = types.InlineKeyboardButton('Удалить фото', callback_data='delete')
    # Кнопка для изменения текста
    btn3 = types.InlineKeyboardButton('Изменить текст', callback_data='edit')
    markup.row(btn2, btn3)
    # Ответ на сообщение с фото/видео
    bot.reply_to(message, 'Какое красивое фото', reply_markup=markup)


# Обработчик нажатий на кнопки встроенной клавиатуры
@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        # Удаление предыдущего сообщения
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        # Изменение текста сообщения
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)


# Запуск бота с непрерывным опросом сервера Telegram
bot.polling(none_stop=True)
