import asyncio
import logging
import re
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from analyzer import smart_analysis
from storage import add_value, get_history

TOKEN = "8910895596:AAG5KfMwTUGvTmFYUGhQhf52b0tQb3NENug"

bot = Bot(token=TOKEN)
dp = Dispatcher()

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📊 Анализ")],
        [KeyboardButton(text="📈 История")],
    ],
    resize_keyboard=True
)

def extract_numbers(text: str):
    matches = re.finditer(r"\d+(\.\d+)?", text)
    return [float(m.group()) for m in matches]


@dp.message()
async def handler(message: types.Message):
    text = message.text

    if text == "/start":
        await message.answer("🤖 Бот запущен", reply_markup=menu)
        return

    if text == "📊 Анализ":
        await message.answer(smart_analysis(get_history()))
        return

    if text == "📈 История":
        await message.answer(str(get_history()[-10:]))
        return

    numbers = extract_numbers(text)

    if numbers:
        for n in numbers:
            add_value(n)

        await message.answer(
            f"📥 Принято: {numbers}\n\n"
            f"{smart_analysis(get_history())}"
        )
        return

    await message.answer("Кинь коэффициенты (например: 1.2 1.5 3.0)")


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
