from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.filters import Text


from apscheduler.schedulers.background import BackgroundScheduler

import asyncio
from everysettings import *
import json

bot = Bot(BOT_ID, parse_mode="HTML")
dp = Dispatcher()
scheduler = BackgroundScheduler()
with open("orders.json") as f:
    curthrasher = json.load(f)['curthr']

@dp.message(Command(commands=['start']))
async def start(message: Message):
    kbthrowout = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='я выкинул(а) мусор')]])
    await message.reply('start', reply_markup=kbthrowout)


@dp.message(Text(text='я выкинул(а) мусор'))
async def throwout(message: Message):
    global curthrasher, dp, bot
    if message.from_user.id == users[curthrasher][1]:
        if curthrasher == len(users)-1:
            curthrasher = 0
        else:
            curthrasher += 1
        with open("orders.json", 'w') as f:
            json.dump({'curthr': curthrasher}, f)
        await bot.send_message(users[curthrasher][1], 'твоя очередь выкидывать мусор!!')

async def main():
    global curthrasher, bot
    await dp.start_polling(bot)


asyncio.run(main())