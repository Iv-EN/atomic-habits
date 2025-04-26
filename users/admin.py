from django.contrib import admin, messages

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_filter = ("id", "email", "username")

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if not obj.tg_chat_id:
            messages.warning(request,
                             "Вы не указали ID телеграм чата. "
                             "Чтобы полноценно использовать приложение, "
                             "перейдите к редактированию профиля и "
                             "укажите tg_chat_id.")
