from rest_framework import serializers

from .models import Habit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        exclude = ["user"]

    def validate(self, attrs):
        instance = self.instance
        if instance:
            for field in attrs:
                if attrs[field] is None:
                    attrs[field] = getattr(instance, field)
        related_habit_id = attrs.get("related_habit")
        if related_habit_id:
                related_habit = Habit.objects.filter(pk=related_habit_id.id).first()
                if related_habit is None or not related_habit.is_pleasant_habit:
                    raise serializers.ValidationError(
                        "Привычка должна быть приятной"
                    )
        habit = Habit(**attrs)
        habit.clean()
        return attrs
