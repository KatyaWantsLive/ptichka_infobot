from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

rules = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'что можно сдать в пункт?', callback_data='what'),
     InlineKeyboardButton(text = 'как правильно сдавать?', callback_data='how')],
     [InlineKeyboardButton(text='На глвную', callback_data='go_home')]
])

back = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Назад', callback_data='back_to_rules')]
])