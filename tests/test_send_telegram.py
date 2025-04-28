from unittest.mock import patch

import pytest
import requests
from django.conf import settings

from core.services import send_telegram_message


@pytest.fixture
def mock_requests_get():
    """
    Изолирует тесты от внешних запросов, предотвращает отправку реальных
    запросов к API Telegram.
    """
    with patch("requests.get") as mock_get:
        yield mock_get


def test_send_telegram_message(mock_requests_get):
    """Проверка отправки сообщения в Telegram."""
    chat_id = "123456"
    message = "Hello, Telegram!"
    send_telegram_message(chat_id, message)
    expected_url = (
        f"{settings.TELEGRAM_URL}{settings.TELEGRAM_BOT_TOKEN}/sendMessage"
    )
    expected_params = {"text": message, "chat_id": chat_id}
    mock_requests_get.assert_called_once_with(
        expected_url, params=expected_params
    )
