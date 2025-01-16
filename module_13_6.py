from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(text="calories")
async def set_age(call):
    await call.message.answer("Введите свой возраст:")
    await UserState.age.set()

    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton(text="Рассчитать")
    button2 = KeyboardButton(text="Информация")
    kb.add(button)
    kb.add(button2)

menu = InlineKeyboardMarkup()
button3 = InlineKeyboardButton(text = 'Рассчитать норму калорий', callback_data='calories')
button4 = InlineKeyboardButton(text = 'Формулы расчёта', callback_data='formulas')
menu.add(button3)
menu.add(button4)

@dp.message_handler(text = "Рассчитать")
async def main_menu(message):
    await message.answer("Выбери опцию:", reply_markup=menu)

@dp.callback_query_handler(text = 'formulas')
async def get_formulas(call):
    await call.message.answer("10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) - 161")
    await call.answer()

@dp.message_handler(commands = ["start"])
async def Start_message(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью", reply_markup=kb)

@dp.message_handler(text = "Рассчитать")
async def inform(message):
    await message.answer("Рассчитать")

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост:")
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес:")
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    age = float(data.get('age'))
    growth = float(data.get('growth'))
    weight = float(data.get('weight'))
    kalori = 10 * weight + 6.25 * growth - 5 * age - 161
    await message.answer(f"Ваша норма калорий: {kalori}")
    await state.finish()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)