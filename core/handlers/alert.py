"""
alert 
"""
import datetime
import logging

from aiogram import Bot, Router
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from alerts_in_ua import AsyncClient as AsyncAlertsClient
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from core.filters.basic import isAdmin
from core.utils.config import ALERTS_TOKEN, DORM_CHAT_ID

router = Router()
lviv_status = "initial"
msg = None


async def alert(bot: Bot):
    global lviv_status
    global msg

    alerts_client = AsyncAlertsClient(token=ALERTS_TOKEN)
    active_alerts = await alerts_client.get_air_raid_alert_statuses_by_oblast()
    # Get the Lviv status
    lviv = str(
        [
            alert
            for alert in active_alerts
            if alert.location_title == "Львівська область"
        ][0]
    )[:-18]
    logging.info(lviv)
    if lviv_status == lviv:
        logging.info("status hasn't changed see ya in 15 seconds")
        return

    if lviv == "alert":
        msg = await bot.send_message(DORM_CHAT_ID, "тривога")
        await bot.pin_chat_message(DORM_CHAT_ID, msg.message_id, True)

    elif msg is not None:
        await bot.send_message(DORM_CHAT_ID, "✅ ВІДБІЙ ТРИВОГИ")
        await bot.unpin_chat_message(DORM_CHAT_ID, msg.message_id)


@router.message(Command("start_api"))
async def check_alert_handler(
    message: Message,
    bot: Bot,
    scheduler: AsyncIOScheduler,
):
    jobs = scheduler.get_jobs()
    if not len(jobs):
        scheduler.add_job(
            alert,
            "interval",
            name="api_parser",
            id="1",
            seconds=15,
            start_date=datetime.datetime.now() + datetime.timedelta(0, 3),
            kwargs={"bot": bot},
        )  # Set the interval as needed
        scheduler.start()
        await message.answer(
            "Scheduler started. Use /stop_api to stop the scheduler.",
            reply_markup=ReplyKeyboardRemove(),
        )
    else:
        await message.answer(
            "You already have the job in progress.\nUse /check_api to check or /stop_api to stop."
        )


@router.message(Command("check_api"), isAdmin())
async def check_jobs_handler(message: Message, scheduler: AsyncIOScheduler):
    jobs = scheduler.get_jobs()
    if len(jobs):
        for job in jobs:
            await message.answer(
                f"Job '{job.name}' with ID {job.id} \nscheduled at: {job.next_run_time}"
            )
    else:
        await message.answer(
            "а ви ще не запускали работягу..", reply_markup=ReplyKeyboardRemove()
        )


@router.message(Command("stop_api"), isAdmin())
async def stop_api_handler(message: Message, scheduler: AsyncIOScheduler):
    scheduler.remove_all_jobs()
    scheduler.shutdown()
    await message.answer("Scheduler stopped.", reply_markup=ReplyKeyboardRemove())
