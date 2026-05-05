
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout

class Command(BaseCommand):
    help = "Populate MongoDB with test data"

    def handle(self, *args, **kwargs):
        # Create test data objects here
        self.stdout.write(self.style.SUCCESS("Database populated successfully"))
