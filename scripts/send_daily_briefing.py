import asyncio

from telegram import Bot

from config import TELEGRAM_BOT_TOKEN
from bot.subscribers import get_subscribers
from news.pipeline import generate_news_briefing


async def send_daily_briefing():

    # Read existing subscribers
    subscribers = get_subscribers()

    if not subscribers:
        raise RuntimeError("No subscribers found in subscribers.json")

    print(
        f"[CLOUD] Found {len(subscribers)} subscribers",
        flush=True
    )

    # Generate briefing once
    print("[CLOUD] Generating daily briefing...", flush=True)

    messages = await asyncio.to_thread(
        generate_news_briefing,
        limit=5
    )

    if not messages:
        raise RuntimeError("No briefing messages generated")

    # Deliver briefing to all subscribers
    async with Bot(token=TELEGRAM_BOT_TOKEN) as bot:

        for chat_id in subscribers:

            print(
                f"[CLOUD] Sending briefing to {chat_id}",
                flush=True
            )

            await bot.send_message(
                chat_id=chat_id,
                text="🚀 TECHPULSE — DAILY TECHNOLOGY BRIEFING"
            )

            for message in messages:
                await bot.send_message(
                    chat_id=chat_id,
                    text=message,
                    disable_web_page_preview=True
                )

    print("[CLOUD] Daily briefing delivered!", flush=True)


if __name__ == "__main__":
    asyncio.run(send_daily_briefing())
