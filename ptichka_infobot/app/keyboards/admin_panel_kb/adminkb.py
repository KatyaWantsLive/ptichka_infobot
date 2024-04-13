from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.db.requests import get_addres, get_event

admin = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '📝Внести изменения', callback_data='make_changes')],
])

changeskb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='💼Места работы', callback_data='work_site'),
     InlineKeyboardButton(text='📅Мероприятия', callback_data='Events')]
])

back = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '↩️Назад', callback_data='back_to_contacts')]
])

work_sitekb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '🗑️Удалить место', callback_data='delete')],
    [InlineKeyboardButton(text = '✏️Добавить новое место', callback_data='add')],
    [InlineKeyboardButton(text = '🔄Изменить текущие', callback_data = 'change_available')],
    [InlineKeyboardButton(text = '↩️Назад', callback_data='to_select')]
])

eventkb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='✏️Добавить мероприятие', callback_data='add_event')],
    [InlineKeyboardButton(text='🗑️Удалить мероприятие', callback_data='delete_event')],
    [InlineKeyboardButton(text = '↩️Назад', callback_data='to_select')]
])

async def addreses():
    all_address = await get_addres()
    keyboard = InlineKeyboardBuilder()
    for address in all_address:
        keyboard.add(InlineKeyboardButton(text = address.street, callback_data = f'address_delete_{address.id}'))
    keyboard.add(InlineKeyboardButton(text = '↩️Назад', callback_data='to_changekb'))    
    return keyboard.adjust(1).as_markup()

async def event():
    all_event = await get_event()
    keyboard = InlineKeyboardBuilder()
    for event in all_event:
        keyboard.add(InlineKeyboardButton(text = event.event_name, callback_data = f'event_{event.id}'))
    keyboard.add(InlineKeyboardButton(text = '↩️Назад', callback_data='to_about_us'))    
    return keyboard.adjust(2).as_markup()
