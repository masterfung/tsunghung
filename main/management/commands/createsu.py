from django.core.management import BaseCommand

__author__ = '@masterfung'

from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser("admin", "thung@me.com", "admin")