import json
from django.core.management.base import BaseCommand
from newapp.models import Movies

class Command(BaseCommand):
    help = "Load mock data from JSON"

    def handle(self, *args, **kwargs):
        with open("mock_data.json") as f:
            data = json.load(f)

        for item in data:
            Movies.objects.get_or_create(**item)

        self.stdout.write(self.style.SUCCESS("Mock data loaded"))
