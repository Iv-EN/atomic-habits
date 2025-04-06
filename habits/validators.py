from rest_framework.serializers import ValidationError

from config.settings import ESTIMATEDDURATION


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
        super().__init__('reward', 'related_habit')

    def __call__(self, value):
        values = self.get_value(value)
        if values["reward"] and values['related_habit']:
            raise ValidationError(
                "Нельзя одновременно указывать вознаграждение "
                "и выбирать связанную привычку (укажите что-то одно)."
            )


class EstimatedDurationValidator(BaseValidator):
    """Проверка времени выполнения привычки."""

    def __init__(self):
        super().__init__('estimated_duration')

    def __call__(self, value):
        val = self.get_value(value)["estimated_duration"]
        if val > ESTIMATEDDURATION:
            raise ValidationError(
                f"Время выполнения привычки не должно превышать "
                f"{ESTIMATEDDURATION} секунд.")


class RelatedHabitValidator(BaseValidator):
    """Проверяет, что связанная привычка - приятная."""

    def __init__(self, field):
        super().__init__("related_habit")

    def __call__(self, value):
        val = self.get_value(value)["related_habit"]
        if val and not val.is_pleasant_habit:
            raise ValidationError(
                "Связанная привычка должна быть приятной"
            )


class PleasantHabitValidator(BaseValidator):
    """
    Проверяет, что у приятной привычки нет вознаграждения
    или связанной привычки.
    """

    def __init__(self, field):
        super().__init__('pleasant_habit')

    def __call__(self, value):
        val = self.get_value(value)["pleasant_habit"]
        if val:
            if (
                    dict(value).get("reward") is not None
                    or dict(value).get("related_habit") is not None
            ):
                raise ValidationError(
                    "У приятной привычки не может быть "
                    "вознаграждения или связанной привычки."
                )


class FrequencyValidator(BaseValidator):
    """
    Проверяет, что периодичность выполнения привычки хотя бы 1 раз в 7 дней.
    """

    def __init__(self, field):
        super().__init__("frequency")

    def __call__(self, value):
        frequency = self.get_value(value)["frequency"]
        if frequency > 7:
            raise ValidationError(
                "Нельзя выполнять привычку реже, чем 1 раз в 7 дней"
            )
