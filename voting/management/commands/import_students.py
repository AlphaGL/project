from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import csv
import os
from django.conf import settings

class Command(BaseCommand):
    help = "Import students from a CSV file and register them"

    def add_arguments(self, parser):
        parser.add_argument(
            'csv_file',
            nargs='?',
            default=os.path.join(settings.BASE_DIR, 'data', 'students.csv'),
            help='Path to the CSV file (default: data/students.csv)'
        )

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        User = get_user_model()

        if not os.path.exists(csv_file):
            self.stdout.write(self.style.ERROR(f"File not found: {csv_file}"))
            return

        with open(csv_file, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for row in reader:
                reg_number = row.get('reg_number')
                full_name = row.get('full_name')
                password = row.get('password')

                if not reg_number or not full_name or not password:
                    self.stdout.write(self.style.WARNING("⚠️ Skipping incomplete row"))
                    continue

                if not User.objects.filter(reg_number=reg_number).exists():
                    User.objects.create_user(
                        reg_number=reg_number,
                        full_name=full_name,
                        password=password
                    )
                    self.stdout.write(
                        self.style.SUCCESS(f"✅ Added {full_name} ({reg_number})")
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING(f"⚠️ {reg_number} already exists, skipping")
                    )
