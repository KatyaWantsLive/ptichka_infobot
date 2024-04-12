from aiogram import F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from loader import router

import app.keyboards.keyboards as kb
import app.db.requests as rq


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Убйете меня нахуй', reply_markup=kb.main)
    await rq.set_user(message.from_user.id)
    await message.answer_sticker('CAACAgIAAxkBAAEEpw5mF95a18_KKLecDsJP8WKI0w2jtgACQkIAAkW6iUhj3hKdzjuC5jQE')

