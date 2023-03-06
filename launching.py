import asyncio
import datetime

from cleaning import *
from trash import *
from moneyreport import *


async def main():
    global curthrasher, bot
    dp.include_router(form_router)
    st_date = datetime.datetime(2023, 3, 13, 21)
    myscheduler.add_job(sendscheduleofroutines, 'interval', days=14, id='sendschedules', start_date=st_date)
    myscheduler.start()
    await dp.start_polling(bot)
    
asyncio.run(main())