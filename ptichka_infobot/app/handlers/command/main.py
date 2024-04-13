from aiogram import F, Router, types
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from loader import router
from loader import dp, bot
from detect import defect


import app.keyboards.commandkb.keyboards as kb
import app.keyboards.admin_panel_kb.adminkb as keyboard
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
import app.db.requests as rq

router = Router()


class Form(StatesGroup):
    photo = State()



@router.message(CommandStart())
async def cmd_start(message: Message):
    await rq.set_user(message.from_user.id)
    if await rq.get_user_status(message.from_user.id) == True:
        await message.answer('Привет! Я телеграм-бот "Птичка", помощник в мире разумного потребления!', reply_markup=kb.main_admin)
    else: await message.answer('Привет! Я телеграм-бот "Птичка", помощник в мире разумного потребления!', reply_markup=kb.main)
    await message.answer_sticker('CAACAgIAAxkBAAEEpw5mF95a18_KKLecDsJP8WKI0w2jtgACQkIAAkW6iUhj3hKdzjuC5jQE')

@router.message(F.text == 'Админ-панель')
async def admin_panel(message: Message):
    if await rq.get_user_status(message.from_user.id) == True:
        await message.answer(f'Добро пожаловать в админ-панель, {message.from_user.first_name}', reply_markup=keyboard.admin)



@router.message(F.text == 'Определить тип вторсырья')
async def photo_detect(message: Message, state: FSMContext):
    await message.answer(f'жду фото...',)
    # await state.set_state(Form.photo)

@router.message(F.photo)
async def photo_detect(message: Message):
    await message.bot.download(file=message.photo[-1].file_id, destination='2.jpg')
    await message.answer(defect('D:/test/ptichka_infobot/2.jpg'))
         

# @router.message(Form.photo)
# async def add_one(message: Message, state: FSMContext):
#     await state.update_data(photo = message.photo[-1].file_id)
#     photo_sizes = await state.get_data()
#     file_id = state.get_data()
#     print(file_id['photo'])
#     # if file_id is None:
#     #     return print('123')
#     # file_info = await bot.get_file(file_id)
#     # downloaded_file = await bot.download_file(file_info.file_path)
#     # with open('photo.jpg', 'wb') as new_file:
#     #     new_file.write(downloaded_file.getvalue())
#     # await state.clear()

