from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.filters import Text
from aiogram import Router

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

import json
from botinits import *

form_router = Router()

class MoneyReport(StatesGroup):
    productname = State()
    productprice = State()


@form_router.message(Command(commands=['returnmoney']))
async def returnmoneycmd(message: Message, state: FSMContext) -> None:
    await state.set_state(MoneyReport.productname)
    await message.answer("напиши что ты купил(а)")

@form_router.message(Command(commands=["cancelrm"]))
async def cancelcmd(message: Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.clear()
    await message.answer("мани репорт отменен^^")

@form_router.message(MoneyReport.productname)
async def typeproductname(message: Message, state: FSMContext):
    await state.update_data(productname=message.text)
    await state.set_state(MoneyReport.productprice)
    await message.answer("напиши сколько это стоило (полностью)")

@form_router.message(MoneyReport.productprice)
async def typeproductprice(message: Message, state: FSMContext) -> None:
    await state.update_data(productprice=message.text)
    if not message.text.isdigit():
        await message.answer("напиши число, а не буквы")
        return
    data = await state.get_data()
    await state.clear()
    print(data)
    allids = [i[1] for i in users]
    senderid = allids.index(message.from_user.id)
    await message.answer("кайф")
    for i in allids[0:senderid]+allids[senderid+1:]:
        await bot.send_message(i, 'тебе надо заплатить за ' + data['productname'] + ' ' + str(int(data['productprice'])/len(users)) + ' от ' + users[senderid][0])