from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Описывает пользователя."""

    email = models.EmailField(unique=True, verbose_name="Электронная почта")
    tg_chat_id = models.CharField(
        max_length=50, verbose_name="Телеграмм чат ID", **settings.NULLABLE
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
