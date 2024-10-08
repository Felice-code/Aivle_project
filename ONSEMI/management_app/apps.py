from django.apps import AppConfig


class ManagementAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "management_app"

    def ready(self):
        import management_app.signals  # 신호 연결

