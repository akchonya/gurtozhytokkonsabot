import logging
import sys
import asyncio
from aiohttp import web
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from core.handlers.start import router as start_router
from core.handlers.basic_link import router as basic_router
from core.handlers.hello import router as hello_router
from core.handlers.weather import router as weather_router
from core.handlers.msg_echo import msg_echo_router, msg_echo_pin_router
from core.handlers.vahta import router as vahta_router
from core.handlers.gumorezka import router as gumorezka_router
from core.handlers.alert import router as alert_router
from core.utils.commands import set_commands
from core.middlewares.apscheduler_mw import SchedulerMiddleware
from core.utils.config import (
    BOT_TOKEN,
    WEB_SERVER_HOST,
    BASE_WEBHOOK_URL,
    WEBHOOK_SECRET,
    WEB_SERVER_PORT,
)


# Path to webhook route, on which Telegram will send requests
WEBHOOK_PATH = f"/bot/{BOT_TOKEN}"
# Secret key to validate requests from Telegram (optional)


async def on_startup(bot: Bot) -> None:
    await set_commands(bot)
    # Set webhook
    await bot.set_webhook(
        f"{BASE_WEBHOOK_URL}{WEBHOOK_PATH}",
        secret_token=WEBHOOK_SECRET,
        allowed_updates=["message", "chat_member"],  # allow updates needed
    )


def main() -> None:
    # Dispatcher is a root router
    dp = Dispatcher()
    scheduler = AsyncIOScheduler()
    dp.update.middleware(SchedulerMiddleware(scheduler))
    dp.include_routers(
        start_router,
        basic_router,
        hello_router,
        weather_router,
        msg_echo_router,
        msg_echo_pin_router,
        vahta_router,
        gumorezka_router,
        alert_router,
    )

    # Register startup hook to initialize webhook
    dp.startup.register(on_startup)
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(BOT_TOKEN, parse_mode=ParseMode.HTML)

    # Create aiohttp.web.Application instance
    app = web.Application()

    # Create an instance of request handler,
    # aiogram has few implementations for different cases of usage
    # In this example we use SimpleRequestHandler which is designed to handle simple cases
    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
        secret_token=WEBHOOK_SECRET,
    )
    # Register webhook handler on application
    webhook_requests_handler.register(app, path=WEBHOOK_PATH)

    # Mount dispatcher startup and shutdown hooks to aiohttp application
    setup_application(app, dp, bot=bot)

    # And finally start webserver
    web.run_app(app, host=WEB_SERVER_HOST, port=WEB_SERVER_PORT)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
