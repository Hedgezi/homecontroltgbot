from apscheduler.schedulers.asyncio import AsyncIOScheduler
import json

from botinits import *

myscheduler = AsyncIOScheduler()

async def sendscheduleofroutines():
    global cleaningoffset
    if cleaningoffset >= len(cleaningwork)-1:
        cleaningoffset = 0
    else:
        cleaningoffset += 1
    for user, work in zip(users, [i for i in cleaningwork[cleaningoffset:len(cleaningwork)] + cleaningwork[0:cleaningoffset]]):
        await bot.send_message(user[1], f'ты делаешь: <b>{work}</b>', parse_mode='HTML')
    with open("states.json", 'w') as f:
        json.dump({'curthr': curthrasher, 'coffset': cleaningoffset}, f)