from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


user_commands = [
    BotCommand(command="faq", description="корисна стаття"),
    BotCommand(command="weather_now", description="погода зараз"),
    BotCommand(command="weather_today", description="прогноз на сьогодні"),
    BotCommand(command="rekvizyty", description="реквізити на оплату за гурт"),
    BotCommand(command="laundry", description="сайт з пралками"),
    # BotCommand(command="gumoreska", description="обрані гуморески"),
    BotCommand(command="svyato", description="свята сьогодні"),
    BotCommand(command="rusoriz", description="ру-со-різ"),
]


async def set_commands(bot: Bot):
    await bot.set_my_commands(user_commands, BotCommandScopeDefault())
