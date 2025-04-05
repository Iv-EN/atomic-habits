# from django.urls import path
# from rest_framework.routers import SimpleRouter
#
# from .apps import HabitsConfig
#
# app_name = HabitsConfig.name

# router = SimpleRouter()
# router.register("", CourseViewSet)
#
# urlpatterns = [
#     path("lessons/", LessonListApiView.as_view(), name="lesson_list"),
#     path(
#         "lessons/<int:pk>/",
#         LessonRetieveApiView.as_view(),
#         name="lesson_retrieve",
#     ),
#     path(
#         "lessons/create/", LessonCreateApiView.as_view(), name="lesson_create"
#     ),
#     path(
#         "lessons/<int:pk>/update/",
#         LessonUpdateApiView.as_view(),
#         name="lesson_update",
#     ),
#     path(
#         "lessons/<int:pk>/delete/",
#         LessonDestroyApiView.as_view(),
#         name="lesson_destroy",
#     ),
# ]
# urlpatterns += router.urls