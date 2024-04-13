from aiogram import F, Router
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from loader import router

import app.keyboards.admin_panel_kb.adminkb as kb
from app.db.requests import delete_address, set_addres, set_event, delete_event


router = Router()

class Add_work(StatesGroup):
    name = State()
    description = State()

class Add_event(StatesGroup):
    name = State()
    description = State()


@router.callback_query(F.data == 'make_changes')
async def make_changes(callback: CallbackQuery):
    print('hello')
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
async def address_delete(callback: CallbackQuery):
    await delete_address(callback.data[15:])
    await callback.answer('')
    await callback.message.edit_text('Что вы хотите сделать?', reply_markup=kb.work_sitekb)


@router.callback_query(F.data.startswith('event_'))
async def address_delete(callback: CallbackQuery):
    await delete_event(callback.data[6:])
    await callback.answer('')
    await callback.message.edit_text('Что вы хотите сделать?', reply_markup=kb.eventkb)


@router.callback_query(F.data == 'to_select')
async def to_select(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Куда внести изменения?', reply_markup=kb.changeskb)

@router.callback_query(F.data == 'delete')
async def delete(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Что нужно удалить?', reply_markup=await kb.addreses())


@router.callback_query(F.data == 'delete_event')
async def delete(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Что нужно удалить?', reply_markup=await kb.event())


@router.callback_query(F.data == 'change_available')
async def change_available(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Что нужно измениьт?', reply_markup=await kb.addreses_to_make())


@router.callback_query(F.data == 'add')
async def add_one(callback: CallbackQuery, state: FSMContext):
    await callback.answer('')
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
    await message.answer('Добавить описание работы', reply_markup=kb.work_sitekb)
    await state.clear()


@router.callback_query(F.data == 'Events')
async def Events(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Что делать?', reply_markup=kb.eventkb)

@router.callback_query(F.data == 'add_event')
async def add_one_event(callback: CallbackQuery, state: FSMContext):
    await callback.answer('')
    await state.set_state(Add_event.name)
    await callback.message.answer('Введите название')


@router.message(Add_event.name)
async def add_two_event(message: Message, state: FSMContext):
    await state.update_data(name = message.text)
    await state.set_state(Add_event.description)
    await message.answer(f'Введите описание мероприятия "перенос на некст строку через ."')


@router.message(Add_event.description)
async def two_three(message: Message, state: FSMContext):
    await state.update_data(description = message.text)
    await set_event(await state.get_data())
    await message.answer('Добавить описание мероприятия', reply_markup=kb.eventkb)
    await state.clear()
