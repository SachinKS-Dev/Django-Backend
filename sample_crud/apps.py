from django.apps import AppConfig


class SampleCrudConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "sample_crud"
    verbose_name = "Sample CRUD (demo)"
