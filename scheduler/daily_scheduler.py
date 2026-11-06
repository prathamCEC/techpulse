import asyncio

from datetime import time
from zoneinfo import ZoneInfo

from telegram.ext import ContextTypes

from config import TIMEZONE
from bot.subscribers import get_subscribers
from news.pipeline import generate_news_briefing


async def daily_news_job(context: ContextTypes.DEFAULT_TYPE):

    print("[SCHEDULER] Daily briefing triggered!", flush=True)

    subscribers = get_subscribers()

    if not subscribers:
        print("[SCHEDULER] No subscribed users found.", flush=True)
        return

    try:
        print("[SCHEDULER] Generating technology briefing...", flush=True)

        messages = await asyncio.to_thread(
            generate_news_briefing,
            limit=5
        )

        for chat_id in subscribers:

            try:
                await context.bot.send_message(
                    chat_id=chat_id,
                    text="🚀 TECHPULSE — DAILY TECHNOLOGY BRIEFING"
                )

                for message in messages:
                    await context.bot.send_message(
                        chat_id=chat_id,
                        text=message,
                        disable_web_page_preview=True
                    )

                print(
                    f"[SCHEDULER] Briefing delivered to {chat_id}",
                    flush=True
                )

            except Exception as error:
                print(
                    f"[SCHEDULER] Delivery failed for {chat_id}: {error}",
                    flush=True
                )

    except Exception as error:
        print(f"[SCHEDULER] Pipeline failed: {error}", flush=True)


def schedule_daily_news(application):

    if application.job_queue is None:
        raise RuntimeError(
            "JobQueue unavailable. Install python-telegram-bot[job-queue]."
        )

    daily_time = time(
        hour=19,
        minute=0,
        tzinfo=ZoneInfo(TIMEZONE)
    )

    application.job_queue.run_daily(
        daily_news_job,
        time=daily_time,
        name="techpulse_daily_briefing"
    )

    print(
        f"[SCHEDULER] Daily briefing scheduled for 7:00 PM {TIMEZONE}",
        flush=True
    )
