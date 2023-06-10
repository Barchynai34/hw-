from aiogram import Bot, Dispatcher, types, executor
from config import token

import random 

bot = Bot(token)
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def start(message:types.Message):
    await message.answer("Я загадал число от 1 до 3 угадайте?")

@dp.message_handler(text=[1,2,3])
async def select(message:types.Message):

        number = random.randint(1,3)
        guess = int(message.text)

        if guess ==number:
               await message.answer(f"Вы угадали. Бот выбрал: {number}")
        else:
            await message.reply(f" Вы проиграли. Бот выбрал: {number}")

executor.start_polling(dp)