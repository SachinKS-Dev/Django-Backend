from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create admin/admin superuser when DEBUG is True (local Docker only)."

    def handle(self, *args, **options):
        if not settings.DEBUG:
            self.stdout.write("Skipping ensure_dev_admin (DEBUG is False).")
            return
        User = get_user_model()
        if User.objects.filter(username="admin").exists():
            self.stdout.write("Superuser admin already exists.")
            return
        User.objects.create_superuser("admin", "admin@localhost", "admin")
        self.stdout.write(self.style.SUCCESS("Created superuser: admin / admin"))
