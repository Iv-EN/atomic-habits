from django.contrib import messages

from tests.base_test_case import BaseTestCase
from users.models import User


class TestUser(BaseTestCase):
    """Тестирование модели User."""

    def test_create_user(self):
        """Проверка создания нового пользователя."""
        data = {
            "username": "new_test_user",
            "email": "test@email.ru",
            "password": "test",
            "tg_chat_id": "123",
        }
        response = self.client.post("/users/register/", data=data)
        assert response.status_code == 201
        assert User.objects.last().username == "new_test_user"
        assert User.objects.count() == 2

    def test_update_user(self):
        """Проверка изменения профиля пользователя."""
        data = {"tg_chat_id": "123"}
        response = self.client.patch("/users/update/", data=data)
        assert response.status_code == 200
        assert User.objects.last().username == "test_user"
        assert User.objects.last().tg_chat_id == "123"

    def test_create_user_with_existing_email(self):
        """Проверка создания пользователя с уже существующим email."""
        data = {
            "username": "new_test_user",
            "email": "test_email",
            "password": "123",
        }
        response = self.client.post("/users/register/", data=data)
        assert response.status_code == 400
        assert "email" in response.data

    def test_user_warning_message(self):
        """Проверка вывода предупреждения, если не указан tg_chat_id."""
        data = {
            "username": "new_test_user",
            "email": "test@email.ru",
            "password": "test",
        }
        response = self.client.post("/users/register/", data=data)
        assert response.status_code == 201
        assert User.objects.last().username == "new_test_user"
        assert response.data["message"] == "Пользователь успешно создан."
        assert "Вы не указали ID телеграм чата" in response.data["warnings"][0]
