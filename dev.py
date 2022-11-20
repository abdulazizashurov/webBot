import os
import django


def setupDjango():
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "admin.settings"
    )
    os.environ.update({"DJANGO_ALLOW_ASYNC_UNSELF": "true"})
    django.setup()


if __name__ == "__main__":
    setupDjango()
    from aiogram import executor
    from src.handlers import dp
    executor.start_polling(dp)
