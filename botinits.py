from aiogram import Bot, Dispatcher
import json

from configs import *

bot = Bot(BOT_ID, parse_mode="HTML")
dp = Dispatcher()

with open("states.json") as f:
    wholejson = json.load(f)
    curthrasher = wholejson['curthr']
    cleaningoffset = wholejson['coffset']