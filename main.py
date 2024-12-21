import telebot
import webbrowser

# Создаем объект бота
bot = telebot.TeleBot('7357624493:AAFAOIvr1JjT0E6jsmUeCLr0bLqQlPjOmds')


# Обработчик команды /site или /website
# Когда пользователь вводит команду /site или /website, открывается указанная ссылка в веб-браузере
@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://www.youtube.com/watch?v=-l_CYgBj4IE&list=PL0lO_mIqDDFUev1gp9yEwmwcy8SicqKbt&index=2')


# Обработчик команд /start, /main или /hello
# Бот отправляет приветственное сообщение с именем и фамилией пользователя
@bot.message_handler(commands=['start', 'main', 'hello'])
def main(message):
    bot.send_message(message.chat.id, f'Hi, {message.from_user.first_name} {message.from_user.last_name}')


# Обработчик команды /help
# Отправляет сообщение с HTML-форматированием, чтобы показать пример помощи
@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>help</b> <em><u>informetion</u></em>', parse_mode='html')


# Обработчик всех остальных сообщений
# Реагирует на определенные тексты: "привет" и "id"
@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        # Если пользователь пишет "привет", бот отвечает с именем и фамилией
        bot.send_message(message.chat.id, f'привет, {message.from_user.first_name} {message.from_user.last_name}')
    elif message.text.lower() == 'id':
        # Если пользователь пишет "id", бот отправляет его имя
        bot.reply_to(message, f'ID: {message.from_user.first_name}')
    # Подготовлено для добавления других условий
    # elif message.test.lower() == ''


# Запуск бота, чтобы он обрабатывал сообщения беспрерывно
bot.polling(none_stop=True)
