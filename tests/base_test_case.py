from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class BaseTestCase(APITestCase):
    """Базовый тестовый класс."""

    def setUp(self):
        """Метод для инициализации тестов."""
        self.user = self.create_user()
        self.habit = self.create_habit()
        self.client.force_authenticate(user=self.user)

    def create_user(self, **kwargs):
        """Создание пользователя с заданными параметрами."""
        default_data = {
            "username": "test_user",
            "email": "test_email",
            "password": "test",
            "tg_chat_id": "123",
        }
        default_data.update(kwargs)
        return User.objects.create(**default_data)

    def create_habit(self, **kwargs):
        """Создание привычки с заданными параметрами."""
        default_data = {
            "habit_action": "Какое-то действие",
            "user": self.user,
            "place": "Где-то",
            "time": "10:00",
            "frequency": 1,
            "estimated_duration": 50,
            "is_pleasant_habit": True,
        }
        default_data.update(kwargs)
        return Habit.objects.create(**default_data)

    def create_habit_data(self, **kwargs):
        """
        Метод для создания данных привычки с учетом переданных параметров.
        """
        default_data = {
            "habit_action": "Тестовое действие",
            "user": self.user.id,
            "place": "Тестовое место",
            "time": "15:00",
            "frequency": 2,
            "estimated_duration": 10,
        }
        default_data.update(kwargs)
        return default_data

    def assert_error_in_response(self, response, error_message):
        """Проверяет наличие сообщения об ошибке в ответе."""
        assert error_message in response.data.get("non_field_errors", [""])[0]
