# Generated by Django 5.2 on 2025-04-05 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "users",
            "0003_rename_tg_id_user_tg_chat_id_remove_user_avatar_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="tg_chat_id",
            field=models.CharField(
                blank=True,
                max_length=50,
                null=True,
                verbose_name="Телеграмм чат ID",
            ),
        ),
    ]
