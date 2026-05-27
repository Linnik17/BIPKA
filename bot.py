import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = "ТВОЙ_ТОКЕН"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# --- КНОПКИ МЕНЮ ---
menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📊 Анализ")],
        [KeyboardButton(text="🎯 Сигнал")],
        [KeyboardButton(text="📈 История")],
    ],
    resize_keyboard=True
)

# --- /start ---
@dp.message()
async def start(message: types.Message):
    if message.text == "/start":
        await message.answer(
            "Бот активирован ⚡\nВыбери действие:",
            reply_markup=menu
        )
        return

    # --- кнопки ---
    if message.text == "📊 Анализ":
        await message.answer(analyze_fake())
    elif message.text == "🎯 Сигнал":
        await message.answer(generate_signal())
    elif message.text == "📈 История":
        await message.answer("История пока пустая 📉")

# --- ЗАГЛУШКИ ЛОГИКИ ---
def analyze_fake():
    return "📊 Анализ: рынок нестабилен, шанс коротких множителей высокий"

def generate_signal():
    import random
    val = round(random.uniform(1.2, 3.5), 2)
    return f"🎯 Сигнал: выход на {val}x"

# --- ЗАПУСК ---
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
