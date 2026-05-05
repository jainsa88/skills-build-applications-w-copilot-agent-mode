from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout

class Command(BaseCommand):
    help = "Populate MongoDB with test data"

    def handle(self, *args, **kwargs):
        # Create test data objects here
        user = User.objects.create(username="testuser", email="testuser@example.com")
        team = Team.objects.create(name="Test Team")
        activity = Activity.objects.create(name="Test Activity")
        workout = Workout.objects.create(user=user, team=team, activity=activity)
        self.stdout.write(self.style.SUCCESS("Database populated successfully"))
