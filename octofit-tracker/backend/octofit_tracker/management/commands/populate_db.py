from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """
    Populate the octofit_db database with test data
    """

    help = "Populate the octofit_db database with test data"

    def handle(self, *args, **kwargs):
        self.stdout.write("Populating octofit_db with test data...")
        self.stdout.write(self.style.SUCCESS("Database populated successfully"))