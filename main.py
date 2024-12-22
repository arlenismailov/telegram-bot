import telebot
import sqlite3
# @fafadafadaaf_bot
# Создаем экземпляр бота с токеном
bot = telebot.TeleBot('7351254259:AAHcfBPP1XVpefets4sHDBJmo1ActRrvMmE')
name = None  # Переменная для хранения имени пользователя


@bot.message_handler(commands=['start'])  # Обработчик команды /start
def start(message):
    # Подключаемся к базе данных или создаем файл базы данных, если его нет
    conn = sqlite3.connect('itproger.sql')
    cur = conn.cursor()

    # Создаем таблицу пользователей, если она не существует
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT, 
            pass TEXT
        )
    ''')
    conn.commit()  # Сохраняем изменения в базе
    cur.close()  # Закрываем курсор
    conn.close()  # Закрываем подключение к базе

    # Отправляем сообщение и запрашиваем имя пользователя
    bot.send_message(message.chat.id, 'Привет, сейчас тебя зарегистрируем! Введите имя!')
    bot.register_next_step_handler(message, user_name)  # Переход к следующему шагу


def user_name(message):
    global name
    name = message.text.strip()  # Сохраняем введенное имя без лишних пробелов
    bot.send_message(message.chat.id, 'Введите пароль')  # Запрашиваем пароль
    bot.register_next_step_handler(message, user_pass)  # Переход к следующему шагу


def user_pass(message):
    password = message.text.strip()  # Сохраняем введенный пароль без лишних пробелов

    # Подключаемся к базе данных
    conn = sqlite3.connect('itproger.sql')
    cur = conn.cursor()

    # Добавляем запись с именем и паролем в таблицу users
    cur.execute(f'INSERT INTO users (name, pass) VALUES ("%s", "%s")' % (name, password))
    conn.commit()  # Сохраняем изменения
    cur.close()  # Закрываем курсор
    conn.close()  # Закрываем подключение к базе

    # Создаем кнопку для отображения списка пользователей
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('Список пользователей', callback_data='users'))
    bot.send_message(message.chat.id, 'Пользователь зарегистрирован!', reply_markup=markup)  # Сообщаем о регистрации


@bot.callback_query_handler(func=lambda call: True)  # Обработчик для нажатий на кнопки
def callback(call):
    # Подключаемся к базе данных
    conn = sqlite3.connect('itproger.sql')
    cur = conn.cursor()

    # Извлекаем всех пользователей из таблицы
    cur.execute('SELECT * FROM users')
    users = cur.fetchall()  # Получаем все строки результата

    # Формируем строку с информацией о пользователях
    info = ''
    for el in users:
        info += f'Имя: {el[1]}, пароль: {el[2]}\n'  # Добавляем имя и пароль каждого пользователя
    cur.close()  # Закрываем курсор
    conn.close()  # Закрываем подключение к базе

    # Отправляем пользователю информацию о всех зарегистрированных
    bot.send_message(call.message.chat.id, info)


# Запускаем бота в режиме непрерывного получения сообщений
bot.polling(none_stop=True)
