from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.db.requests import get_event ,get_addres

about_us = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Как мы работаем?', callback_data='how_work'),
     InlineKeyboardButton(text = 'Мероприятия', callback_data='Event')],
     [InlineKeyboardButton(text='На глвную', callback_data='go_home')]
])

back_to_address = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад', callback_data='to_address')]
])

back_to_event = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад', callback_data='to_event')]
])



async def event():
    all_event = await get_event()
    keyboard = InlineKeyboardBuilder()
    for event in all_event:
        keyboard.add(InlineKeyboardButton(text = event.event_name, callback_data = f'event_{event.id}'))
    keyboard.add(InlineKeyboardButton(text = 'Назад', callback_data='to_about_us'))    
    return keyboard.adjust(2).as_markup()

async def addreses():
    all_address = await get_addres()
    keyboard = InlineKeyboardBuilder()
    for address in all_address:
        keyboard.add(InlineKeyboardButton(text = address.street, callback_data = f'address_{address.id}'))
    keyboard.add(InlineKeyboardButton(text = 'Назад', callback_data='to_about_us'))    
    return keyboard.adjust(1).as_markup()