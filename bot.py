import asyncio
import logging
import random
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from analyzer import analyze_market, generate_signal
from storage import add_value, get_history

TOKEN = "8910895596:AAG5KfMwTUGvTmFYUGhQhf52b0tQb3NENug"

bot = Bot(token=TOKEN)
dp = Dispatcher()

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📊 Анализ")],
        [KeyboardButton(text="🎯 Сигнал")],
        [KeyboardButton(text="📈 История")],
    ],
    resize_keyboard=True
)

@dp.message()
async def handler(message: types.Message):
    text = message.text

    if text == "/start":
        await message.answer("🤖 Бот запущен", reply_markup=menu)

    elif text == "📊 Анализ":
        await message.answer(analyze_market())

    elif text == "🎯 Сигнал":
        await message.answer(generate_signal(get_history()))

    elif text == "📈 История":
        hist = get_history()
        await message.answer(f"📊 Последние значения:\n{hist[-10:]}")

    else:
        # имитация новых коэффициентов (потом заменишь на парсинг)
        val = round(random.uniform(1.1, 5.0), 2)
        add_value(val)

        await message.answer(f"📥 Новое значение добавлено: {val}x")

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
