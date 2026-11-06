
import asyncio

from telegram import Update
from telegram.ext import ContextTypes

from news.pipeline import generate_news_briefing


async def start_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    await update.message.reply_text(
        "🚀 Welcome to TechPulse!\n\n"
        "Your personal technology news assistant.\n\n"
        "Available commands:\n"
        "/news - Latest technology news\n"
        "/ai - AI developments\n"
        "/start - Restart the bot\n\n"
        "Stay informed. Stay curious. Stay ahead."
    )

    print(f"Chat ID: {update.effective_chat.id}")


async def news_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    print("[BOT] /news command received!", flush=True)

    await update.message.reply_text(
        "🔍 Fetching technology news and generating AI summaries..."
    )

    try:

        print("[BOT] Calling news pipeline...", flush=True)

        messages = await asyncio.to_thread(
            generate_news_briefing
        )

        print("[BOT] Pipeline completed!", flush=True)

        await update.message.reply_text(
            "🚀 TECHPULSE — TECHNOLOGY BRIEFING"
        )

        for message in messages:

            await update.message.reply_text(
                message,
                disable_web_page_preview=True
            )

    except Exception as error:

        print(f"News command error: {error}", flush=True)

        await update.message.reply_text(
            "Something went wrong while preparing your briefing. Please try again."
        )
