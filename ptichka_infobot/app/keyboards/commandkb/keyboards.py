from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Правила сдачи'),
    KeyboardButton(text='Определить тип вторсырья')],
    [KeyboardButton(text='Контакты'),
    KeyboardButton(text='О нас')]],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню...')
main_admin = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Правила сдачи'),
     KeyboardButton(text='Контакты')],
    [KeyboardButton(text='О нас'),
    KeyboardButton(text='Админ-панель')],
    [KeyboardButton(text='Определить тип вторсырья')]],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню...')
