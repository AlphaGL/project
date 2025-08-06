from django.core.management.base import BaseCommand
from voting.models import Student
from django.contrib.auth.hashers import make_password

class Command(BaseCommand):
    help = 'Add specific students with registration numbers, full names, and passwords'

    def handle(self, *args, **kwargs):
        # List of students to be added
        students = [
            {'reg_number': '20231428501', 'full_name': 'John Doe', 'password': 'password123'},
            {'reg_number': '20231428502', 'full_name': 'Jane Smith', 'password': 'password456'},
            {'reg_number': '20231428503', 'full_name': 'Alice Johnson', 'password': 'password789'},
            {'reg_number': '20231428504', 'full_name': 'Bob Williams', 'password': 'passwordABC'},
            {'reg_number': '20231428505', 'full_name': 'Emily Brown', 'password': 'passwordDEF'},
            {'reg_number': '20231428506', 'full_name': 'Michael Davis', 'password': 'passwordGHI'},
            {'reg_number': '20231428507', 'full_name': 'Emma Taylor', 'password': 'passwordJKL'},
            {'reg_number': '20231428508', 'full_name': 'Luke Moore', 'password': 'passwordMNO'},
            {'reg_number': '20231428509', 'full_name': 'Sarah Anderson', 'password': 'passwordPQR'},
            {'reg_number': '20231428510', 'full_name': 'David Thomas', 'password': 'passwordSTU'},
            {'reg_number': '20231428511', 'full_name': 'Daniel Jackson', 'password': 'passwordVWX'},
            {'reg_number': '20231428512', 'full_name': 'Olivia White', 'password': 'passwordYZA'},
            {'reg_number': '20231428513', 'full_name': 'Sophia Harris', 'password': 'passwordBCD'},
            {'reg_number': '20231428514', 'full_name': 'James Martin', 'password': 'passwordEFG'},
            {'reg_number': '20231428515', 'full_name': 'Ethan Thompson', 'password': 'passwordHIJ'},
            {'reg_number': '20231428516', 'full_name': 'Isabella Garcia', 'password': 'passwordKLM'},
            {'reg_number': '20231428517', 'full_name': 'Liam Martinez', 'password': 'passwordNOP'},
            {'reg_number': '20231428518', 'full_name': 'Ava Robinson', 'password': 'passwordQRS'},
            {'reg_number': '20231428519', 'full_name': 'Noah Clark', 'password': 'passwordTUV'},
            {'reg_number': '20231428520', 'full_name': 'Mia Rodriguez', 'password': 'passwordWXY'},
            {'reg_number': '20231428583', 'full_name': 'Chukwugozirim Ibeawuchi', 'password': 'passwordZ123'},
            {'reg_number': '20231428584', 'full_name': 'Nneka Ibeawuchi', 'password': 'password456Z'},
        ]

        # Iterate over the list of students
        for student_data in students:
            reg_number = student_data['reg_number']
            full_name = student_data['full_name']
            password = make_password(student_data['password'])

            # Check if the student already exists
            if not Student.objects.filter(reg_number=reg_number).exists():
                # Create a new student entry
                Student.objects.create(
                    reg_number=reg_number,
                    full_name=full_name,
                    password=password
                )
                self.stdout.write(self.style.SUCCESS(f'Successfully added {full_name} with reg number {reg_number}'))
            else:
                self.stdout.write(self.style.WARNING(f'Registration number {reg_number} already exists, skipping'))
