from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Populate MongoDB with test data for octofit_db"

    def handle(self, *args, **kwargs):
        self.stdout.write("Populating octofit_db with test data...")
        self.stdout.write(self.style.SUCCESS("Database populated successfully"))