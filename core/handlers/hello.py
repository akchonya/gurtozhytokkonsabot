"""
    replies "ні", "Ні", "нІ", "НІ" messages
"""


from aiogram import Router, F
from aiogram.types import ReplyKeyboardRemove, Message

router = Router()


hi = ("ні", "Ні", "НІ", "нІ")
hello = ("неllo", "Неllo", "HELLO", "нELLO")


@router.message(F.text.in_(hi))
async def hi_handler(message: Message):
    await message.reply(
        hello[hi.index(message.text)], reply_markup=ReplyKeyboardRemove()
    )
