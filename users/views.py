from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet


class UserViewSet(ModelViewSet):
    """ViewSet для работы с пользователями."""

