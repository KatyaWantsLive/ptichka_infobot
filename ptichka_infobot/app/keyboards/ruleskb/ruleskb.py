from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

rules = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Типы вторсырья', callback_data='what'),
     InlineKeyboardButton(text = 'Правила сдачи', callback_data='how')],
     [InlineKeyboardButton(text='На главную', callback_data='go_home')]
])

back = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Назад', callback_data='back_to_rules')]
])
