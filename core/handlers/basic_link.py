"""
/faq sends a link to the FAQ article
"""


from aiogram import types, Router
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardRemove


router = Router()


@router.message(Command("faq"))
async def faq_handler(message: types.Message):
    await message.answer(
        "🧾 https://telegra.ph/stattya-gurt-11-08", reply_markup=ReplyKeyboardRemove()
    )


@router.message(Command("rekvizyty"))
async def rekvizyty_handler(message: types.Message):
    await message.answer("реквізити тут", reply_markup=ReplyKeyboardRemove())


@router.message(Command("laundry"))
async def laundry_handler(message: types.Message):
    await message.answer(
        "🧺 https://chudovend.bilantek.com/?tcn=102", reply_markup=ReplyKeyboardRemove()
    )
