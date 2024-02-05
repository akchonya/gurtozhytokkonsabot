"""
Commands to send stickers to the chat
"""


from random import randint

from aiogram import Router, types
from aiogram.filters import Command

router = Router()


@router.message(Command("bunt"))
async def bunt_sticker(message: types.Message):
    await message.answer_sticker(
        sticker="CAACAgIAAxkBAAEYRLBjKfNf9QtXKpeiBrBcSp5BNP2rwAACKiEAAgnVUUlHhGyMxOT0wykE"
    )


@router.message(Command("rusoriz"))
async def rusorizt_sticker(message: types.Message):
    stickers = (
        "CAACAgIAAxkBAAEouIZlmyH78U-XzgbGxcVSZY8rykCLjAAC2xEAAheC6EjvAoFgb4_29jQE",
        "CAACAgIAAxkBAAEmExNlCHyRvioQXW0ipPfqt9SK1nxGfwACUDcAAggFQEhQ1W5cnK9FlzAE",
    )
    await message.answer_sticker(stickers[randint(0, 1)])
