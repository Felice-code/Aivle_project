from django.apps import AppConfig


class MonitoringAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "monitoring_app"
    
    def ready(self):
        import monitoring_app.signals
