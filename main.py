# Импортируем необходимые классы и функции из библиотеки aiogram
from aiogram import Bot, Dispatcher, executor, types
# @fafafafafaeweww_bot
# Создаем экземпляр бота с токеном
bot = Bot('7222878978:AAF9VNR2rrzV-u3W9XyEDIyP2xdKiACc2po')

# Создаем диспетчер для обработки сообщений и других событий
dp = Dispatcher(bot)


# Обработчик сообщений с содержимым типа "фото"
@dp.message_handler(content_types=['photo'])  # Указываем, что обрабатываем только сообщения с фото
async def start(message: types.Message):
    # Отправляем ответное сообщение с текстом "Hello"
    await message.reply('Hello')
    # Пример кода для отправки фото (закомментирован):
    # file = open('/some.png', 'rb')
    # await message.answer_photo(file)


# Обработчик команды "/inline"
@dp.message_handler(commands=['inline'])
async def info(message: types.Message):
    # Создаем разметку для встроенных кнопок
    markup = types.InlineKeyboardMarkup()
    # Добавляем кнопку, которая ведет на сайт
    markup.add(types.InlineKeyboardButton('Site', url='https://itproger.com'))
    # Добавляем кнопку с callback-данными
    markup.add(types.InlineKeyboardButton('Hello', callback_data='hello'))
    # Отправляем сообщение с кнопками
    await message.reply('Hello', reply_markup=markup)


# Обработчик callback-запросов (нажатие на Inline-кнопки)
@dp.callback_query_handler()
async def callback(call):
    # Отправляем сообщение с callback-данными, которые содержались в кнопке
    await call.message.answer(call.data)


# Обработчик команды "/reply"
@dp.message_handler(commands=['reply'])
async def reply(message: types.Message):
    # Создаем разметку для кнопок, отображающихся прямо в чате
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)  # Клавиатура исчезает после выбора
    # Добавляем кнопки "Site" и "Website"
    markup.add(types.KeyboardButton('Site'))
    markup.add(types.KeyboardButton('Website'))
    # Отправляем сообщение с кнопками
    await message.answer('Hello', reply_markup=markup)


# Запуск бота с использованием метода start_polling
executor.start_polling(dp)
