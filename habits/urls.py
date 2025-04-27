from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .apps import HabitsConfig
from .views import HabitViewSet, PublicHabitListView

app_name = HabitsConfig.name

router = SimpleRouter()
router.register("", HabitViewSet)

urlpatterns = [
    path(
        "public-habits/", PublicHabitListView.as_view(), name="public_habits"
    ),
    path("", include(router.urls)),
]
