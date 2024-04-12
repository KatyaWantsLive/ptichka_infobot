from aiogram import F
from aiogram.types import Message, CallbackQuery
from loader import router

import app.keyboards.ruleskb.ruleskb as kb

@router.message(F.text == 'Правила сдачи')
async def about_us(message: Message):
    await message.delete()
    await message.answer('Правила сдачи', reply_markup=kb.rules)

@router.callback_query(F.data == 'what')
async def cooperation(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('https://vk.com/ptichka_punkt?w=wall-216486932_1025', reply_markup=kb.back)

@router.callback_query(F.data == 'how')
async def cooperation(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('https://vk.com/ptichka_punkt?w=wall-216486932_676', reply_markup=kb.back)

@router.callback_query(F.data == 'back_to_rules')
async def back(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Правила сдачи', reply_markup=kb.rules)

@router.callback_query(F.data == 'go_home')
async def back(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.delete()