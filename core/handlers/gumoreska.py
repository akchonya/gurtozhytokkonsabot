"""
/gumoreska sends a joke to the chat
"""


from random import randint

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove

router = Router()

gumoresky = (
    "купіл мужик шляпу а она єму как раз",
    "уявімо що тут прикол номер 2",
    "тут от мій улюблений анекдот про простітутку яка сосе і співає, знаєте такий?",
    "тут ще ось анекдот про наприклад їжачка в лісі",
)


@router.message(Command("gumoreska"))
async def gumoreska_handler(message: Message):
    await message.answer(
        gumoresky[randint(0, len(gumoresky) - 1)], reply_markup=ReplyKeyboardRemove()
    )
