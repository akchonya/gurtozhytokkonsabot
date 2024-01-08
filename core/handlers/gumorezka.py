"""
/gumorezka sends a joke to the chat
"""


from random import randint

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove

router = Router()

gumorezky = (
    "купіл мужик шляпу а она єму как раз",
    "уявімо що тут прикол номер 2",
    "тут от мій улюблений анекдот про простітутку яка сосе і співає, знаєте такий?",
    "тут ще ось анекдот про наприклад їжачка в лісі",
)


@router.message(Command("gumorezka"))
async def gumorezka_handler(message: Message):
    await message.answer(
        gumorezky[randint(0, len(gumorezky) - 1)], reply_markup=ReplyKeyboardRemove()
    )
