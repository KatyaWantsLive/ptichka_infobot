from aiogram import F
from aiogram.types import Message, CallbackQuery
from loader import router


import app.keyboards.contactkb as kb


@router.message(F.text == 'Контакты')
async def about_us(message: Message):
    await message.delete()
    await message.answer('Контакты', reply_markup=kb.contacts)

@router.callback_query(F.data == 'questions')
async def cooperation(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Номер телефона: 89322484552 \nГруппа в вк: https://vk.com/ptichka_punkt', reply_markup=kb.back)

@router.callback_query(F.data == 'back_to_contacts')
async def back(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Контакты', reply_markup=kb.contacts)

@router.callback_query(F.data == 'go_home')
async def go_home(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.delete()