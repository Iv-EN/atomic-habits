from habits.models import Habit
from tests.base_test_case import BaseTestCase


class TestHabits(BaseTestCase):
    """Тестирование модели Habit."""

    def setUp(self):
        super().setUp()
        self.related_habit = self.create_habit(habit_action="Действие")

    def test_create_habit(self):
        """Проверка создания привычки."""
        data = self.create_habit_data()
        response = self.client.post("/habits/", data=data)
        assert response.status_code == 201
        assert Habit.objects.last().habit_action == "Тестовое действие"
        assert Habit.objects.count() == 3

    def test_estimated_duration(self):
        """
        Проверка, что указанное время выполнения привычки не более заданного.
        """
        data = {"estimated_duration": 200}
        response = self.client.put(f"/habits/{self.habit.id}/", data=data)
        assert response.status_code == 400

    def test_invalid_pleasant_habit(self):
        """
        Проверяет, что у приятной привычки не может быть вознаграждения или
        связанной привычки.
        """
        test_cases = [
            {
                "data": {"reward": "Вознаграждение"},
                "error_message": "У приятной привычки не может быть вознаграж",
            },
            {
                "data": {"related_habit": 1},
                "error_message": "У приятной привычки не может быть вознаграж",
            },
        ]
        for case in test_cases:
            data = self.create_habit_data(
                is_pleasant_habit=True, **case["data"]
            )
            response = self.client.post("/habits/", data=data)
            assert response.status_code == 400
            self.assert_error_in_response(response, case["error_message"])

    def test_reward_and_related_habit(self):
        """
        Проверяет одновременное наличие связанной привычки и вознаграждения.
        """
        data = self.create_habit_data(
            reward="Вознаграждение",
            related_habit=self.related_habit.id
        )
        response = self.client.post("/habits/", data=data)
        print(f"Ответ - {response.data}")
        assert response.status_code == 400
        self.assert_error_in_response(response, "Нельзя одновременно ук")

    def test_frequency(self):
        """Проверка периода выполнения привычки."""
        data = {"frequency": 10}
        response = self.client.patch(f"/habits/{self.habit.id}/", data=data)
        assert response.status_code == 400
        assert "Убедитесь, что это значение м" in response.data["frequency"][0]

    def test_str_habit(self):
        """Проверка метода __str__ модели Habit."""
        expected_str = (
            f"{self.habit.id} - {self.habit.habit_action}, "
            f"время - {self.habit.time}, место выполнения - {self.habit.place}"
        )
        assert str(self.habit) == expected_str
