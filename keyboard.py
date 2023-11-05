from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import types


def main_menu():
    code = KeyboardButton('Зашифровать 🔒')
    un_code = KeyboardButton('Расшифровать 🔓')

    greet_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    greet_kb.add(code, un_code)
    return greet_kb


from aiogram import types


def more():
    keyboard = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton("Назад🔙", callback_data='more')
    keyboard.add(button)
    return keyboard
