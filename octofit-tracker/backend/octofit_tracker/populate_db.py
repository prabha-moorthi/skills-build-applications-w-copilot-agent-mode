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
    team = Team.objects.create(name="Octo Ninjas")

    user = User.objects.create(
        username="testuser",
        email="testuser@octofit.com",
        team=team
    )

    Activity.objects.create(
        user=user,
        activity_type="Running",
        duration=30
    )

    Workout.objects.create(
        name="Morning Cardio",
        calories_burned=300
    )

    Leaderboard.objects.create(
        user=user,
        total_points=100
    )

    print("✅ Database populated with test data")

if __name__ == "__main__":
    populate()
