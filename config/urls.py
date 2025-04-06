from django.contrib import admin
from django.urls import include, path

from users.apps import UsersConfig
from habits.apps import HabitsConfig


urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls", namespace=UsersConfig.name)),
    path("habits/", include("habits.urls", namespace=HabitsConfig.name)),
]
