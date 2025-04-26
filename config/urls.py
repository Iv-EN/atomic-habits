from django.contrib import admin
from django.urls import include, path

from habits.apps import HabitsConfig
from users.apps import UsersConfig

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls", namespace=UsersConfig.name)),
    path("habits/", include("habits.urls", namespace=HabitsConfig.name)),
]
