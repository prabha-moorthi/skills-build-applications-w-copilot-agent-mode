from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.response import Response
from rest_framework.decorators import api_view

from octofit_tracker import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'teams', views.TeamViewSet)
router.register(r'activities', views.ActivityViewSet)
router.register(r'workouts', views.WorkoutViewSet)
router.register(r'leaderboard', views.LeaderboardViewSet)


@api_view(["GET"])
def api_root(request):
    return Response({
        "users": request.build_absolute_uri("/api/users/"),
        "teams": request.build_absolute_uri("/api/teams/"),
        "activities": request.build_absolute_uri("/api/activities/"),
        "workouts": request.build_absolute_uri("/api/workouts/"),
        "leaderboard": request.build_absolute_uri("/api/leaderboard/"),
    })


urlpatterns = [
    path("", api_root),
    path("api/", include(router.urls)),
    path("admin/", admin.site.urls),
]
