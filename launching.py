import asyncio

# from cleaning import *
from trash import *


async def main():
    global curthrasher, bot
    # myscheduler.add_job(sendscheduleofroutines, 'interval', seconds=10, id='sendschedules')
    # myscheduler.start()
    await dp.start_polling(bot)
    
asyncio.run(main())