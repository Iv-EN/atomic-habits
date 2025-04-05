from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """Создаёт пользователя."""

    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(serializer.validated_data.get("password"))
        if user.tg_chat_id is None:
            print(
                "Вы не указали ID телеграм чата."
                "Что бы полноценно использовать приложение перейдете "
                "к редактированию профиля и укажите tg_chat_id."
            )
        user.is_active = True
        user.save()


class UserUpdateAPIView(generics.RetrieveUpdateAPIView):
    """
    Представление для получения и редактирования профиля текущего пользователя.
    """

    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_user(self):
        """Получает текущего пользователя."""
        return self.request.user

    def update(self, request, *args, **kwargs):
        """Обновляет профиль пользователя."""
        user = self.get_user()
        serializer = self.get_serializer(
            user, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)
