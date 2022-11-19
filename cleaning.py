from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.filters import Text
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import json

from botinits import *

myscheduler = AsyncIOScheduler()
cleaningoffset = 0

async def sendscheduleofroutines():
    global cleaningoffset
    if cleaningoffset >= len(cleaningwork)-1:
        cleaningoffset = 0
    else:
        cleaningoffset += 1
    for user, work in zip(users, [i for i in cleaningwork[cleaningoffset:len(cleaningwork)] + cleaningwork[0:cleaningoffset]]):
        await bot.send_message(user[1], f'ты делаешь: <b>{work}</b>', parse_mode='HTML')