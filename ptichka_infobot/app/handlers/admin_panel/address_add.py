from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery
from aiogram import F, Router

router = Router()

class Add_work(StatesGroup):
    name = State()
    description = State()


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
