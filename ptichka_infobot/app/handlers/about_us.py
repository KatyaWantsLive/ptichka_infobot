from aiogram import F
from aiogram.types import Message, CallbackQuery
from loader import router


import app.keyboards.about_uskb as kb
from app.db.requests import get_address_description

@router.message(F.text == 'О нас')
async def about_us(message: Message):
    await message.delete()
    await message.answer('О нас', reply_markup=kb.about_us)


@router.callback_query(F.data == 'to_about_us')
async def to_about_us(callback: CallbackQuery):
    await callback.message.edit_text('О нас', reply_markup=kb.about_us)

@router.callback_query(F.data == 'go_home')
async def go_home(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.delete()

@router.callback_query(F.data == 'how_work')
async def how_work(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Как мы работаем?', reply_markup=await kb.addreses())

@router.callback_query(F.data.startswith('address_'))
async def address_description(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text((await get_address_description(callback.data[8:])).replace('.', '\n'), reply_markup=kb.back_to_address)

@router.callback_query(F.data == 'to_address')
async def back_to_addres(callback: CallbackQuery):
    await callback.message.edit_text('Как мы работаем?', reply_markup=await kb.addreses())