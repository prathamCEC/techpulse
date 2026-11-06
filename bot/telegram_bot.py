
from telegram.ext import Application, CommandHandler

from config import TELEGRAM_BOT_TOKEN
from bot.commands import start_command, news_command, stop_command
from scheduler.daily_scheduler import schedule_daily_news


def run_bot():

    application = (
        Application.builder()
        .token(TELEGRAM_BOT_TOKEN)
        .build()
    )

    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("news", news_command))
    application.add_handler(CommandHandler("stop", stop_command))

    # Register the daily briefing job
    schedule_daily_news(application)

    print("TechPulse Telegram bot is running...")

    application.run_polling()
