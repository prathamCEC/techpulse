import json
from pathlib import Path


SUBSCRIBERS_FILE = Path(__file__).with_name("subscribers.json")


def get_subscribers():
    if not SUBSCRIBERS_FILE.exists():
        return []

    try:
        with SUBSCRIBERS_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError) as error:
        print(f"[SUBSCRIBERS] Could not read subscribers: {error}")
        return []


def subscribe(chat_id):
    subscribers = get_subscribers()

    if chat_id not in subscribers:
        subscribers.append(chat_id)

        with SUBSCRIBERS_FILE.open("w", encoding="utf-8") as file:
            json.dump(subscribers, file, indent=4)

        print(f"[SUBSCRIBERS] Added chat: {chat_id}")


def unsubscribe(chat_id):
    subscribers = get_subscribers()

    if chat_id in subscribers:
        subscribers.remove(chat_id)

        with SUBSCRIBERS_FILE.open("w", encoding="utf-8") as file:
            json.dump(subscribers, file, indent=4)

        print(f"[SUBSCRIBERS] Removed chat: {chat_id}")
