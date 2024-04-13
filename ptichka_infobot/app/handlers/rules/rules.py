from aiogram import F, types
from aiogram.types import Message, CallbackQuery, InputMediaPhoto, FSInputFile
from loader import router
from photo_paths import jpg_paths, jpg_paths1
from loader import bot
from aiogram.utils.media_group import MediaGroupBuilder

import app.keyboards.ruleskb.ruleskb as kb

@router.message(F.text == '📜Правила сдачи')
async def about_us(message: Message):
    await message.delete()
    await message.answer('Правила сдачи', reply_markup=kb.rules)

@router.callback_query(F.data == 'what')
async def cooperation(callback: CallbackQuery):
    media_group1 = MediaGroupBuilder(caption="")
    for path in jpg_paths1:
        media_group1.add_photo(FSInputFile(path))
    await callback.answer('')
    await bot.send_media_group(chat_id=callback.message.chat.id, media=media_group1.build())
    await callback.message.answer('Типы вторсырья', reply_markup=kb.back)

@router.callback_query(F.data == 'how')
async def cooperation(callback: CallbackQuery): 
    media_group = MediaGroupBuilder(caption="")
    for path in jpg_paths:
        media_group.add_photo(FSInputFile(path))
    await callback.answer('')
    await bot.send_media_group(chat_id=callback.message.chat.id, media=media_group.build())
    await callback.message.answer('Правила сдачи', reply_markup=kb.back)

@router.callback_query(F.data == 'back_to_rules')
async def back(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Правила сдачи', reply_markup=kb.rules)

@router.callback_query(F.data == 'go_home')
async def back(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.delete()