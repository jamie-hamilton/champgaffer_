"""Run populate database command"""
from generators.generator import populate_database
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """Populate datebase via command"""
    def handle(self, *args, **options):
        populate_database()
