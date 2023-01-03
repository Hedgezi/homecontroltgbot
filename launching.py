import asyncio
import datetime

from cleaning import *
from trash import *
from moneyreport import *


async def main():
    global curthrasher, bot
    dp.include_router(form_router)
    myscheduler.add_job(sendscheduleofroutines, 'interval', days=7, id='sendschedules', start_date=datetime.datetime(2022, 11, 21, 21))
    myscheduler.start()
    await dp.start_polling(bot)
    
asyncio.run(main())