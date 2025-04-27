import requests
from django.conf import settings


def send_telegram_message(chat_id, message):
    """Отправляет напоминания в Telegram."""
    params = {
        "text": message,
        "chat_id": chat_id,
    }
    requests.get(
        f"{settings.TELEGRAM_URL}{settings.TELEGRAM_BOT_TOKEN}/sendMessage",
        params=params,
    )
