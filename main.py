import telebot
import webbrowser

# Создаем объект бота
bot = telebot.TeleBot('7357624493:AAFAOIvr1JjT0E6jsmUeCLr0bLqQlPjOmds')


@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://www.youtube.com/watch?v=-l_CYgBj4IE&list=PL0lO_mIqDDFUev1gp9yEwmwcy8SicqKbt&index=2')


@bot.message_handler(commands=['start', 'main', 'hello'])
def main(message):
    bot.send_message(message.chat.id, f'Hi, {message.from_user.first_name} {message.from_user.last_name}')


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>help</b> <em><u>informetion</u></em>', parse_mode='html')


@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'привет, {message.from_user.first_name} {message.from_user.last_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.first_name}')
    # elif message.test.lower() == ''


bot.polling(none_stop=True)
