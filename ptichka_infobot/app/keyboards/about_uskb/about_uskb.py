from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.db.requests import get_addres

about_us = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Как мы работаем?', callback_data='how_work'),
     InlineKeyboardButton(text = 'Мероприятия', callback_data='how')],
     [InlineKeyboardButton(text='На глвную', callback_data='go_home')]
])

back_to_address = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад', callback_data='to_address')]
])

async def addreses():
    all_address = await get_addres()
    keyboard = InlineKeyboardBuilder()
    for address in all_address:
        keyboard.add(InlineKeyboardButton(text = address.street, callback_data = f'address_{address.id}'))
    keyboard.add(InlineKeyboardButton(text = 'Назад', callback_data='to_about_us'))    
    return keyboard.adjust(1).as_markup()