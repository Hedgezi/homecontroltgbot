from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.filters import Text
import json

from botinits import *

@dp.message(Command(commands=['info']))
async def infocmd(message: Message):
    await message.reply("я работаю \n© kolya, from 2022 to eternity", parse_mode="HTML")

@dp.message(Command(commands=['whoseturn']))
async def whoseturncmd(message: Message):
    for i in range(len(users)):
        if users[i][1] == message.from_user.id:
            askeduser = i
    await message.reply(f"сейчас очередь: {users[curthrasher][0]} \nтвоя очередь будет через: {askeduser - curthrasher if askeduser >= curthrasher else len(users) - curthrasher + askeduser}")

@dp.message(Text(text='я выкинул(а) мусор'))
async def throwout(message: Message):
    global curthrasher, dp, bot
    if message.from_user.id == users[curthrasher][1]:
        if curthrasher == len(users)-1:
            curthrasher = 0
        else:
            curthrasher += 1
        with open("states.json", 'w') as f:
            json.dump({'curthr': curthrasher, 'coffset': cleaningoffset}, f)
        kbthrowout = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='я выкинул(а) мусор')]])
        await message.reply("молодец, твой пирожок - 🍔", reply_markup=ReplyKeyboardRemove)
        await bot.send_message(users[curthrasher][1], 'твоя очередь выкидывать мусор!! 🗑️🗑️🗑️', reply_markup=kbthrowout)
