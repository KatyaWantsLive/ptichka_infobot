from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

contacts = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Остались вопросы?', callback_data='questions'),
     InlineKeyboardButton(text = 'Хотите сотрудничать?', url='https://inlnk.ru/YAzPA0')],
     [InlineKeyboardButton(text='На глвную', callback_data='go_home')]
])

back = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Назад', callback_data='back_to_contacts')]
])