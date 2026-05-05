from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(name="Test User", email="test@example.com", team="marvel")
        self.assertEqual(user.name, "Test User")
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.team, "marvel")

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name="marvel", description="Marvel Team")
        self.assertEqual(team.name, "marvel")
        self.assertEqual(team.description, "Marvel Team")

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(name="Test User", email="test2@example.com", team="dc")
        activity = Activity.objects.create(user=user, activity_type="run", duration=30, date="2023-01-01")
        self.assertEqual(activity.user, user)
        self.assertEqual(activity.activity_type, "run")
        self.assertEqual(activity.duration, 30)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name="Pushups", description="Upper body", suggested_for="marvel")
        self.assertEqual(workout.name, "Pushups")
        self.assertEqual(workout.suggested_for, "marvel")

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name="dc", description="DC Team")
        leaderboard = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(leaderboard.team, team)
        self.assertEqual(leaderboard.points, 100)
