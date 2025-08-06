from django.core.management.base import BaseCommand
from voting.models import Position, Contestant

class Command(BaseCommand):
    help = 'Create initial positions and contestants'

    def handle(self, *args, **kwargs):
        positions = [
            {'name': 'President', 'importance': 1},
            {'name': 'Vice President', 'importance': 2},
            {'name': 'Secretary', 'importance': 3},
            {'name': 'Treasurer', 'importance': 4}
        ]

        contestants = [
            {'position_name': 'President', 'name': 'John Doe'},
            {'position_name': 'President', 'name': 'Jane Smith'},
            {'position_name': 'Vice President', 'name': 'Alice Johnson'},
            {'position_name': 'Vice President', 'name': 'Bob Williams'},
            {'position_name': 'Secretary', 'name': 'Emily Brown'},
            {'position_name': 'Secretary', 'name': 'Michael Davis'},
            {'position_name': 'Treasurer', 'name': 'Emma Taylor'},
            {'position_name': 'Treasurer', 'name': 'Luke Moore'}
        ]

        # Create positions
        for position_data in positions:
            Position.objects.get_or_create(name=position_data['name'], defaults={'importance': position_data['importance']})
            self.stdout.write(self.style.SUCCESS(f'Successfully added position {position_data["name"]}'))

        # Create contestants
        for contestant_data in contestants:
            position = Position.objects.get(name=contestant_data['position_name'])
            Contestant.objects.get_or_create(position=position, name=contestant_data['name'])
            self.stdout.write(self.style.SUCCESS(f'Successfully added contestant {contestant_data["name"]} for position {contestant_data["position_name"]}'))
