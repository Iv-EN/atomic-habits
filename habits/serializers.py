from rest_framework import serializers

from .models import Habit

from core.validators import (
    PleasantHabitValidator,
    RewardValidator,
)


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        exclude = ["user"]
        validators = [
            PleasantHabitValidator(),
            RewardValidator(),
        ]
