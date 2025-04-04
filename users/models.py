from django.contrib.auth.models import AbstractUser
from django.db import models

blank_null_true = {"blank": True, "null": True}


class User(AbstractUser):
    """Описывает пользователя."""

    email = models.EmailField(unique=True, verbose_name="Электронная почта")
    tg_chat_id = models.CharField(
        max_length=50, **blank_null_true, verbose_name="Телеграмм ID"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
