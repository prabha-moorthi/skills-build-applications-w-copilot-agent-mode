import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "octofit_tracker.settings")
django.setup()

from tracker.models import (
    User,
    Team,
    Activity,
    Workout,
    Leaderboard
)

def populate():
    team1 = Team.objects.create(name="Octo Ninjas")
    team2 = Team.objects.create(name="Fit Krakens")

    user1 = User.objects.create(
        username="testuser1",
        email="testuser1@octofit.com",
        team=team1
    )

    user2 = User.objects.create(
        username="testuser2",
        email="testuser2@octofit.com",
        team=team2
    )

    Activity.objects.create(
        user=user1,
        activity_type="Running",
        duration=30
    )

    Activity.objects.create(
        user=user2,
        activity_type="Cycling",
        duration=45
    )

    Workout.objects.create(
        name="Morning Cardio",
        calories_burned=300
    )

    Workout.objects.create(
        name="Evening Strength",
        calories_burned=450
    )

    Leaderboard.objects.create(
        user=user1,
        total_points=100
    )

    Leaderboard.objects.create(
        user=user2,
        total_points=150
    )

    print("✅ Database populated with test data")

    
    
    if __name__ == "__main__": populate()

