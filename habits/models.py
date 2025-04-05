from django.db import models

from config.settings import NULLABLE
from users.models import User


class Habit(models.Model):
    """Описывает привычку."""

    habit_action = models.CharField(
        max_length=255, verbose_name="Действие привычки"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Создатель привычки"
    )
    place = models.CharField(
        max_length=255, verbose_name="Место выполнения привычки"
    )
    time = models.TimeField(verbose_name="Время выполнения привычки")
    is_pleasant_habit = models.BooleanField(
        default=False, verbose_name="Признак приятной привычки"
    )
    related_habit = (
        models.ForeignKey(
            "self",
            **NULLABLE,
            on_delete=models.SET_NULL,
            verbose_name="Связанная привычка",
        ),
    )
    frequency = models.PositiveIntegerField(
        default=1,
        verbose_name="Периодичность выполнения",
        help_text="Количество выполнений привычки в неделю"
    )
    reward = models.CharField(
        max_length=255, **NULLABLE, verbose_name="Вознаграждение за выполнение"
    )
    estimated_duration = models.PositiveIntegerField(
        verbose_name="Время на выполнение в минутах"
    )
    is_public = models.BooleanField(
        default=False, verbose_name="Признак публичности"
    )

    def __str__(self):
        return (
            f"{self.user} - {self.habit_action} at {self.time} in {self.place}"
        )
