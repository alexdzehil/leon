from django.apps import AppConfig


class BarConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bar'
    verbose_name = 'Конфигурация сайта'
