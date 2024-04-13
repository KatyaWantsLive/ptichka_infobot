from aiogram import F, Router
from aiogram.types import Message, CallbackQuery


router = Router()

import app.keyboards.about_uskb.about_uskb as kb
from app.db.requests import get_address_description, get_event_description

@router.message(F.text == 'О нас')
async def about_us(message: Message):
    await message.delete()
    await message.answer('О нас', reply_markup=kb.about_us)


@router.callback_query(F.data == 'Event')
async def event(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Ивенты', reply_markup = await kb.event())

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

@router.callback_query(F.data.startswith('event_'))
async def address_description(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text((await get_event_description(callback.data[6:])).replace('.', '\n'), reply_markup=kb.back_to_event)


@router.callback_query(F.data.startswith('address_'))
async def address_description(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text((await get_address_description(callback.data[8:])).replace('.', '\n'), reply_markup=kb.back_to_address)

@router.callback_query(F.data == 'to_address')
async def back_to_addres(callback: CallbackQuery):
    await callback.message.edit_text('Как мы работаем?', reply_markup=await kb.addreses())

@router.callback_query(F.data == 'to_event')
async def back_to_addres(callback: CallbackQuery):
    await callback.message.edit_text('Как мы работаем?', reply_markup=await kb.event())