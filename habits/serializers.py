from rest_framework import serializers

from core.validators import PleasantHabitValidator, RewardValidator
from habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        exclude = ["user"]
        validators = [
            PleasantHabitValidator(),
            RewardValidator(),
        ]
