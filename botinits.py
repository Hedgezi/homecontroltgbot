from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.filters import Text
# from apscheduler.schedulers.background import BackgroundScheduler

import asyncio, json
from configs import *

bot = Bot(BOT_ID, parse_mode="HTML")
dp = Dispatcher()

with open("orders.json") as f:
    curthrasher = json.load(f)['curthr']