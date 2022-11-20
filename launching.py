import asyncio
import datetime, zoneinfo

from cleaning import *
from trash import *


async def main():
    global curthrasher, bot
    # myscheduler.add_job(sendscheduleofroutines, 'interval', days=7, id='sendschedules', start_date=datetime.datetime(2022, 11, 21, 21, tzinfo=zoneinfo.ZoneInfo("Europe/Prague")))
    myscheduler.add_job(sendscheduleofroutines, 'interval', seconds=10, id='sendschedules', start_date=datetime.datetime(2022, 11, 21, 0, 21, tzinfo=zoneinfo.ZoneInfo("Europe/Prague")))
    myscheduler.start()
    await dp.start_polling(bot)
    
asyncio.run(main())