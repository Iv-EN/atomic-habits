from django.core.exceptions import ValidationError
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
    related_habit = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        limit_choices_to={"is_pleasant_habit": True},
        verbose_name="Связанная привычка",
        help_text="Может быть только приятной (is_pleasant_habit: True)"
    )
    frequency = models.PositiveIntegerField(
        default=1,
        verbose_name="Периодичность выполнения",
        help_text="Периодичность выполнения привычки в днях"
    )
    reward = models.CharField(
        max_length=255, **NULLABLE, verbose_name="Вознаграждение за выполнение"
    )
    estimated_duration = models.PositiveIntegerField(
        verbose_name="Время на выполнение в секундах",
        help_text="Введите время на выполнение в секундах."
    )
    is_public = models.BooleanField(
        default=False, verbose_name="Признак публичности"
    )

    def __str__(self):
        return (
            f"{self.id} - {self.habit_action}, время - {self.time}, "
            f"место выполнения - {self.place}"
        )

    def clean(self):
        if self.reward and self.related_habit:
            raise ValidationError(
                "Нельзя одновременно заполнять вознаграждение "
                "и связанную привычку."
            )
        if self.is_pleasant_habit:
            if self.reward or self.related_habit:
                raise ValidationError(
                    "У приятной привычки не может быть "
                    "вознаграждения или связанной привычки."
                )
        if self.estimated_duration is not None and self.estimated_duration > 120:
            raise ValidationError(
                "Время выполнения должно быть не больше 120 секунд"
            )
        if self.frequency is not None and self.frequency > 7:
            raise ValidationError(
                "Нельзя выполнять привычку реже, чем 1 раз в 7 дней"
            )
        if self.related_habit and not self.related_habit.is_pleasant_habit:
            raise ValidationError("Привычка должна быть приятной")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)