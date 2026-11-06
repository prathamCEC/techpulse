
import asyncio

from telegram import Update
from telegram.ext import ContextTypes

from news.pipeline import generate_news_briefing
from bot.subscribers import subscribe, unsubscribe


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    chat_id = update.effective_chat.id
    subscribe(chat_id)

    await update.message.reply_text(
        "🚀 Welcome to TechPulse!\n\n"
        "Your personal technology news assistant.\n\n"
        "Get curated updates covering:\n"
        "🤖 Artificial Intelligence\n"
        "🚀 Startups and Big Tech\n"
        "💻 Software and Developer Tools\n"
        "🔐 Cybersecurity\n"
        "📱 Hardware and Gadgets\n"
        "🔬 Science and Emerging Technology\n\n"
        "Available commands:\n"
        "/news - Get the latest technology briefing\n"
        "/stop - Unsubscribe from daily briefings\n\n"
        "📅 Daily briefing: 7:00 PM IST\n\n"
        "Stay informed. Stay curious. Stay ahead."
    )


async def stop_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    unsubscribe(update.effective_chat.id)

    await update.message.reply_text(
        "You've unsubscribed from TechPulse daily briefings. "
        "Use /start whenever you want to subscribe again."
    )


async def news_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "🔍 Fetching technology news and generating AI summaries..."
    )

    try:
        messages = await asyncio.to_thread(
            generate_news_briefing,
            limit=5
        )

        await update.message.reply_text(
            "🚀 TECHPULSE — TECHNOLOGY BRIEFING"
        )

        for message in messages:
            await update.message.reply_text(
                message,
                disable_web_page_preview=True
            )

    except Exception as error:

        print(f"[BOT] News command error: {error}", flush=True)

        await update.message.reply_text(
            "Something went wrong while preparing your briefing. Please try again."
        )
