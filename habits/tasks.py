from datetime import timedelta

from celery import shared_task
from django.utils import timezone

from core.services import send_telegram_message
from habits.models import Habit
from users.models import User


@shared_task
def collect_data_for_reminders():
    """Собирает информацию для отправки напоминаний за 1 час до выполнения."""
    print("Задача запускается!")
    now = timezone.now()
    print(f"Время сейчас {now}")
    one_hour_later = now + timedelta(hours=1)
    users_with_tg_chat_id = User.objects.filter(tg_chat_id__isnull=False)
    for user in users_with_tg_chat_id:
        print(f"{user.tg_chat_id}, {user.username}")
        habits = Habit.objects.filter(
            user=user,
            is_pleasant_habit=False,
            time__gte=now.time(),
            time__lt=one_hour_later.time(),
        )
        for habit in habits:
            print(f"{habit.habit_action}, {user.tg_chat_id}")
            related_habit_action = (
                habit.related_habit.habit_action
                if habit.related_habit
                else None
            )
            message = (
                f"Уважаемый {user.username}, "
                f"напоминаю Вам о необходимости раз в {habit.frequency} дней "
                f"в {habit.time} часов, место выполнения - {habit.place} "
                f"выполнять привычку '{habit.habit_action}'. "
                f"После чего Вас ждёт выполнение приятной привычки "
                f"'{related_habit_action or 'нет'}' "
                f"или вознаграждение '{habit.reward or 'нет'}'"
            )
            print(message)
            send_telegram_message(int(user.tg_chat_id), message)
