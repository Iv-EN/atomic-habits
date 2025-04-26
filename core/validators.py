from rest_framework.serializers import ValidationError


class BaseValidator:
    """Базовый класс для валидаторов."""

    def __init__(self, *args):
        self.fields = args

    def get_value(self, value):
        return {field: dict(value).get(field) for field in self.fields}

    def call(self, value):
        raise NotImplementedError("Метод должен быть описан в наследниках.")


class RewardValidator(BaseValidator):
    """Проверяет одновременный выбор связанной привычки и вознаграждения."""

    def __init__(self):
        super().__init__("reward", "related_habit")

    def __call__(self, value):
        reward = value.get("reward")
        related_habit = value.get("related_habit")
        if reward and related_habit:
            raise ValidationError(
                "Нельзя одновременно указывать вознаграждение "
                "и выбирать связанную привычку (укажите что-то одно)."
            )


class PleasantHabitValidator(BaseValidator):
    """
    Проверяет, что у приятной привычки нет вознаграждения
    или связанной привычки.
    """

    def __init__(self):
        super().__init__("is_pleasant_habit")

    def __call__(self, value):
        val = self.get_value(value)["is_pleasant_habit"]
        if val:
            if (
                dict(value).get("reward") is not None
                or dict(value).get("related_habit") is not None
            ):
                raise ValidationError(
                    "У приятной привычки не может быть "
                    "вознаграждения или связанной привычки."
                )
