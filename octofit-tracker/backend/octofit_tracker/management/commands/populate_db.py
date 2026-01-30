from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create Users
        users = [
            User.objects.create(email='ironman@marvel.com', name='Iron Man', team=marvel.name),
            User.objects.create(email='captainamerica@marvel.com', name='Captain America', team=marvel.name),
            User.objects.create(email='batman@dc.com', name='Batman', team=dc.name),
            User.objects.create(email='superman@dc.com', name='Superman', team=dc.name),
        ]

        # Create Workouts
        workouts = [
            Workout.objects.create(name='Strength Training', description='Full body strength', difficulty='Hard'),
            Workout.objects.create(name='Cardio Blast', description='High intensity cardio', difficulty='Medium'),
        ]

        # Create Activities
        Activity.objects.create(user=users[0], type='Running', duration=30, date=date.today())
        Activity.objects.create(user=users[1], type='Cycling', duration=45, date=date.today())
        Activity.objects.create(user=users[2], type='Swimming', duration=60, date=date.today())
        Activity.objects.create(user=users[3], type='Yoga', duration=40, date=date.today())

        # Create Leaderboard
        Leaderboard.objects.create(user=users[0], score=100, rank=1)
        Leaderboard.objects.create(user=users[1], score=90, rank=2)
        Leaderboard.objects.create(user=users[2], score=80, rank=3)
        Leaderboard.objects.create(user=users[3], score=70, rank=4)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
