from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from loader import router

import app.keyboards.commandkb.keyboards as kb
import app.keyboards.admin_panel_kb.adminkb as keyboard
import app.db.requests as rq

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await rq.set_user(message.from_user.id)
    if await rq.get_user_status(message.from_user.id) == True:
        await message.answer('Привет! Я телеграм-бот "Птичка, помощник в мире разумного потребления!', reply_markup=kb.main_admin)
    else: await message.answer('Привет! Я телеграм-бот "Птичка, помощник в мире разумного потребления!', reply_markup=kb.main)
    await message.answer_sticker('CAACAgIAAxkBAAEEpw5mF95a18_KKLecDsJP8WKI0w2jtgACQkIAAkW6iUhj3hKdzjuC5jQE')

@router.message(F.text == 'Админ панель')
async def admin_panel(message: Message):
    if await rq.get_user_status(message.from_user.id) == True:
        await message.answer(f'Добро пожаловать в админ-панель, {message.from_user.first_name}', reply_markup=keyboard.admin)
