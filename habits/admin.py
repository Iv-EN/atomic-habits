from django.contrib import admin

from .models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_filter = ("user", "is_pleasant_habit", "is_public")
