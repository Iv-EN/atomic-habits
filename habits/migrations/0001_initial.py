# Generated by Django 5.2 on 2025-04-03 19:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Habit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "habit_action",
                    models.CharField(
                        max_length=255, verbose_name="Действие привычки"
                    ),
                ),
                (
                    "place",
                    models.CharField(
                        max_length=255,
                        verbose_name="Место выполнения привычки",
                    ),
                ),
                (
                    "time",
                    models.TimeField(verbose_name="Время выполнения привычки"),
                ),
                (
                    "is_pleasant_habit",
                    models.BooleanField(
                        default=False, verbose_name="Признак приятной привычки"
                    ),
                ),
                (
                    "frequency",
                    models.PositiveIntegerField(
                        default=1, verbose_name="Периодичность выполнения"
                    ),
                ),
                (
                    "reward",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Вознаграждение за выполнение",
                    ),
                ),
                (
                    "estimated_duration",
                    models.PositiveIntegerField(
                        verbose_name="Время на выполнение в минутах"
                    ),
                ),
                (
                    "is_public",
                    models.BooleanField(
                        default=False, verbose_name="Признак публичности"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Создатель привычки",
                    ),
                ),
            ],
        ),
    ]
