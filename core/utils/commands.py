from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


user_commands = [
    BotCommand(command="faq", description="корисна стаття"),
    BotCommand(command="vahta", description="графік вахтерів"),
    BotCommand(command="weather_now", description="погода зараз"),
    BotCommand(command="weather_today", description="прогноз на сьогодні"),
    BotCommand(command="rekvizyty", description="реквізити на оплату за гурт"),
    BotCommand(command="laundry", description="сайт з пралками"),
    BotCommand(command="vahta", description="розклад вахтерів"),
    BotCommand(command="gumorezka", description="обрані гуморезки"),
]


async def set_commands(bot: Bot):
    await bot.set_my_commands(user_commands, BotCommandScopeDefault())
