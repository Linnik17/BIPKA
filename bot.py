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

def extract_number(text: str):
    match = re.search(r"(\d+(\.\d+)?)", text)
    if match:
        return float(match.group(1))
    return None


@dp.message()
async def handler(message: types.Message):
    text = message.text

    # старт
    if text == "/start":
        await message.answer("🤖 Crash Analyzer активирован", reply_markup=menu)
        return

    # кнопки
    if text == "📊 Анализ":
        await message.answer(smart_analysis(get_history()))
        return

    if text == "📈 История":
        await message.answer(f"📊 Последние значения:\n{get_history()[-10:]}")
        return

    # 🔥 если пользователь кидает число или сообщение
    number = extract_number(text)

    if number:
        add_value(number)
        await message.answer(
            f"📥 Принято: {number}x\n\n{smart_analysis(get_history())}"
        )
        return

    # если ссылка
    if "http" in text:
        await message.answer(
            "🌐 Ссылка принята.\nПока анализ ссылок в разработке, но скоро подключим парсер 🚀"
        )
        return

    await message.answer("Кинь коэффициент (например 2.3) или ссылку 🌐")


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
