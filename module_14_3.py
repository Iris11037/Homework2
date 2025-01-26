from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(KeyboardButton('Рассчитать'))
kb.add(KeyboardButton('Информация'))
kb.add(KeyboardButton('Купить'))

menu = InlineKeyboardMarkup()
menu.add(InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories'))
menu.add(InlineKeyboardButton('Формулы расчёта', callback_data='formulas'))

menu2 = InlineKeyboardMarkup()
menu2.add(InlineKeyboardButton('Продукт1', callback_data="product_buying"))
menu2.add(InlineKeyboardButton('Продукт2', callback_data="product_buying"))
menu2.add(InlineKeyboardButton('Продукт3', callback_data="product_buying"))
menu2.add(InlineKeyboardButton('Продукт4', callback_data="product_buying"))

@dp.message_handler(commands = ["start"])
async def start_message(message: types.Message):
    await message.answer('Привет! Я бот помогающий твоему здоровью. Для расчета калорий нажмите "Рассчитать".', reply_markup=kb)

@dp.message_handler(text = "Рассчитать")
async def main_menu(message: types.Message):
    await message.answer("Выбери опцию:", reply_markup=menu)

@dp.callback_query_handler(text = 'formulas')
async def get_formulas(call: types.CallbackQuery):
    await call.message.answer("10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) - 161")
    await call.answer()

@dp.callback_query_handler(text = "calories")
async def set_age(call: types.CallbackQuery):
    await call.message.answer("Введите свой возраст:", reply_markup=types.ReplyKeyboardRemove())
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=int(message.text))
    await message.answer("Введите свой рост:")
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=int(message.text))
    await message.answer("Введите свой вес:")
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=int(message.text))
    data = await state.get_data()
    age = float(data.get('age'))
    growth = float(data.get('growth'))
    weight = float(data.get('weight'))
    kalori = 10 * weight + 6.25 * growth - 5 * age - 161
    await message.answer(f"Ваша норма калорий: {kalori}")
    await state.finish()

@dp.message_handler(text = 'Купить')
async def get_buying_list(message: types.Message):
    for i in range(1,5):
        await message.answer(f"Название: Продукт {i} | Описание: описание{i}  | Цена: {i * 100}")
        with open(f"Tabletki_{i}.jpg", "rb") as img:
            await message.answer_photo(img)
    await message.answer("Выберите продукт для покупки:", reply_markup=menu2)

@dp.callback_query_handler(text = 'product_buying')
async def send_confirm_message(call: types.CallbackQuery):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)