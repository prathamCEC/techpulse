from telegram.ext import Application, CommandHandler

from config import TELEGRAM_BOT_TOKEN
from bot.commands import start_command, news_command


def run_bot():

    application = (
        Application.builder()
        .token(TELEGRAM_BOT_TOKEN)
        .build()
    )

    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("news", news_command))

    print("TechPulse Telegram bot is running...")

    application.run_polling()
