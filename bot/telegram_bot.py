from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes
)

from config import TELEGRAM_BOT_TOKEN
from bot.commands import start_command, news_command


async def send_message(chat_id, message, bot=None):

    try:

        if bot is None:
            raise ValueError("Bot instance is required")

        await bot.send_message(
            chat_id=chat_id,
            text=message,
            disable_web_page_preview=True
        )

        print("Telegram message sent successfully!")

    except Exception as error:

        print(f"Telegram delivery error: {error}")


def run_bot():

    application = (
        Application.builder()
        .token(TELEGRAM_BOT_TOKEN)
        .build()
    )

    application.add_handler(
        CommandHandler("start", start_command)
    )

    application.add_handler(
        CommandHandler("news", news_command)
    )

    print("TechPulse Telegram bot is running...")

    application.run_polling()
