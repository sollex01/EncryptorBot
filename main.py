from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message

from code import codding, decoding
from keyboards import main_menu

TOKEN = 'Ваш токен'

bot = Bot(token=TOKEN)

dp = Dispatcher(bot)

current_mode = None


# Обработчики кнопок
@dp.message_handler(commands=['start'])
async def start(message: Message):
    global current_mode
    current_mode = None
    await bot.send_message(message.chat.id, 'Привет выбери режим', reply_markup=main_menu())


@dp.message_handler(commands=['help'])
async def start(message: Message):
    await bot.send_message(message.chat.id,
                           'шифровка меняется каждые 24 часа, все анонимно, есть более 50 видов шифра.')


@dp.message_handler(lambda x: x.text == 'Зашифровать 🔒')
async def code(message: Message):
    global current_mode
    current_mode = 'code'
    await bot.send_message(message.chat.id, 'Введите сообщение которое хотите зашифровать')


@dp.message_handler(lambda x: x.text == 'Расшифровать 🔓')
async def decode(message: Message):
    global current_mode
    current_mode = 'decode'
    await bot.send_message(message.chat.id, 'Сообщение которое хотите расшифровать')


@dp.message_handler(content_types=['text'])
async def handle_text(message: Message):
    print(message.text)
    global current_mode
    if current_mode == 'code':
        await bot.send_message(message.chat.id, codding(message.text))
    elif current_mode == 'decode':
        await bot.send_message(message.chat.id, decoding(message.text))
    else:
        await bot.send_message(message.chat.id, 'Пожалуйста, выберите режим из меню')


executor.start_polling(dp)
