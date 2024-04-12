from aiogram import F, Router
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from loader import router

import app.keyboards.admin_panel_kb.adminkb as kb
from app.db.requests import delete_work_site
from app.db.requests import set_addres

router = Router()

class Add_work(StatesGroup):
    name = State()
    description = State()


@router.callback_query(F.data == 'make_changes')
async def make_changes(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Куда внести изменения?', reply_markup=kb.changeskb)
    

@router.callback_query(F.data == 'work_site')
async def work_site(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Что вы хотите сделать?', reply_markup=kb.work_sitekb)


@router.callback_query(F.data == 'to_changekb')
async def to_changekb(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Что вы хотите сделать?', reply_markup=kb.work_sitekb)


@router.callback_query(F.data.startswith('address_delete_'))
async def address_description(callback: CallbackQuery):
    await delete_work_site(callback.data[15:])
    await callback.answer('')
    await callback.message.edit_text('Что вы хотите сделать?', reply_markup=kb.work_sitekb)


@router.callback_query(F.data == 'to_select')
async def to_select(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Куда внести изменения?', reply_markup=kb.changeskb)


@router.callback_query(F.data == 'delete')
async def delete(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('сука что удалить надо то блять?', reply_markup=await kb.addreses())


@router.callback_query(F.data == 'change_available')
async def change_available(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('выбери что менять пидор', reply_markup=await kb.addreses_to_make())

@router.callback_query(F.data == 'add')
async def add_one(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Add_work.name)
    await callback.message.answer('Введите улицу')


@router.message(Add_work.name)
async def add_two(message: Message, state: FSMContext):
    await state.update_data(name = message.text)
    await state.set_state(Add_work.description)
    await message.answer(f'Введите график работы "перенос на некст строку через ."')


@router.message(Add_work.description)
async def two_three(message: Message, state: FSMContext):
    await state.update_data(description = message.text)
    await set_addres(await state.get_data())
    await message.answer('Пошел нахуй', reply_markup=kb.work_sitekb)
    await state.clear()
