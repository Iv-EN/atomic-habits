from datetime import timedelta
from unittest.mock import patch

from django.utils import timezone

from habits.models import Habit
from habits.tasks import collect_data_for_reminders
from tests.base_test_case import BaseTestCase


class TestTasks(BaseTestCase):
    """Тестирование задачи по отправке напоминаний."""

    def test_collect_data_for_reminders(self):
        """Тестирование сбора информации для отправки напоминаний."""
        now = timezone.now()
        habit_time = (now + timedelta(minutes=30)).time()
        habit = Habit.objects.create(
            user=self.user,
            is_pleasant_habit=False,
            time=habit_time,
            frequency=1,
            place="Дом",
            habit_action="Прочитать книгу",
            estimated_duration=25,
        )
        with patch("habits.tasks.send_telegram_message") as mock_send_message:
            collect_data_for_reminders()
        assert mock_send_message.called
        expected_message = (
            f"Уважаемый {self.user.username}, "
            f"напоминаю Вам о необходимости раз в {habit.frequency} дней "
            f"в {habit.time} часов, место выполнения - {habit.place} "
            f"выполнять привычку '{habit.habit_action}'. "
            f"После чего Вас ждёт выполнение приятной привычки "
            f"'нет' "
            f"или вознаграждение 'нет'"
        )
        mock_send_message.assert_called_with(
            int(self.user.tg_chat_id), expected_message
        )
