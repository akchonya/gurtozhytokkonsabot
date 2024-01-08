"""
/update_vahta updates vahta picture
"""

from aiogram import Bot, F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove, Message, FSInputFile
from core.filters.basic import isAdmin
from core.utils.statesvahta import StatesVahta


router = Router()


@router.message(Command("vahta"))
async def vahta_handler(message: Message):
    photo = FSInputFile("vahta.png")
    await message.answer_photo(
        photo=photo,
        caption="Прошу! Усе що знаю про графік наших (ваших) вахтерів:",
        reply_markup=ReplyKeyboardRemove(),
    )


@router.message(isAdmin(), Command("update_vahta"))
async def get_photo(message: Message, state: FSMContext):
    await message.answer(
        "Send a photo or /cancel to cancel.",
        reply_markup=ReplyKeyboardRemove(),
    )
    await state.set_state(StatesVahta.GET_PHOTO)


# A cancelation option
@router.message(isAdmin(), StatesVahta.GET_PHOTO, Command("cancel"))
@router.message(isAdmin(), StatesVahta.GET_PHOTO, F.text.casefold() == "cancel")
async def cancel_handler(message: Message, state: FSMContext) -> None:
    """
    Allow user to cancel any action
    """
    current_state = await state.get_state()
    if current_state is None:
        return

    await state.clear()
    await message.answer(
        "/update_vahta is cancelled.",
        reply_markup=ReplyKeyboardRemove(),
    )


@router.message(StatesVahta.GET_PHOTO)
async def save_photo(message: Message, state: FSMContext, bot: Bot):
    # Saving the picture locally
    fileID = message.photo[-1].file_id
    file_info = await bot.get_file(fileID)
    downloaded_file = await bot.download_file(file_info.file_path)

    with open("vahta.png", "wb") as new_file:
        new_file.write(downloaded_file.getvalue())

    # Sending admin a success message
    await message.answer("Done. Use /vahta to check")
    await state.clear()
