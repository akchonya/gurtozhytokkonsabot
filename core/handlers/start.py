"""
/start greets users
"""


from aiogram import types, Router
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardRemove


router = Router()


@router.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer(
        "привіт! я ботік-помічник чату гурту львівської музичної академії 😎\n\n"
        "якщо вам потрібен власний телеграм бот - звертайся до @FleshkaXDude",
        reply_markup=ReplyKeyboardRemove(),
    )
