"""
alert 
"""


from aiogram import Bot, Router, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from alerts_in_ua import AsyncClient as AsyncAlertsClient
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from core.utils.config import ALERTS_TOKEN
from core.filters.basic import isAdmin

router = Router()


async def alert(bot: Bot, alert_status: str):
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
    print(lviv)
    print(alert_status)


@router.message(Command("test"))
async def test(
    message: Message, bot: Bot, scheduler: AsyncIOScheduler, dispatcher: Dispatcher
):
    # TODO
    pass


@router.message(Command("start_api"))
async def check_alert_handler(
    message: Message, bot: Bot, scheduler: AsyncIOScheduler, alert_status: str
):
    jobs = scheduler.get_jobs()
    if not len(jobs):
        scheduler.add_job(
            alert,
            "interval",
            name="api_parser",
            id="1",
            seconds=15,
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
    await message.answer("Scheduler stopped.", reply_markup=ReplyKeyboardRemove())
