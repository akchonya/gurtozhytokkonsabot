"""
/faq sends a link to the FAQ article
"""


from aiogram import types, Router
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardRemove
from core.utils.soup import parse_page

router = Router()


@router.message(Command("faq"))
async def faq_handler(message: types.Message):
    await message.answer(
        "📝 https://telegra.ph/stattya-gurt-11-08",
        reply_markup=ReplyKeyboardRemove(),
    )


@router.message(Command("rekvizyty"))
async def rekvizyty_handler(message: types.Message):
    text = "<b>Реквізити для оплати за навчання:</b>\n\nЛНМА імені М.В.Лисенка\np/p UA888201720313281004201001387\n\nДКСУ у м. Київ\n\nЄДРПОУ 02214225\n\nПризначення платежу: за навчания студента ПІП (Обовʼязково вказувати ПІП студента)\n\n\n<b>Оплата за проживання в гуртожитку:</b>\n\nЛНМА імені М.В.Лисенка\np/p UA898201720313251004202001387\n\nДКСУ у м. Київ\n\nЄДРПОУ 02214225\n\nПризначення платежу: за гуртожиток студента ПІП (Обовʼязково вказувати ПІП студента)"
    await message.answer(text, reply_markup=ReplyKeyboardRemove())


@router.message(Command("laundry"))
async def laundry_handler(message: types.Message):
    await message.answer(
        "🧺 https://chudovend.bilantek.com/?tcn=102",
        reply_markup=ReplyKeyboardRemove(),
        disable_web_page_preview=True,
    )


@router.message(Command("svyato"))
async def svyaro_handler(message: types.Message):
    svyato = await parse_page("https://daytoday.ua/sogodni/")
    await message.answer(
        f"🍾 <b>свята сьогодні:</b>\n{svyato}", reply_markup=ReplyKeyboardRemove()
    )
