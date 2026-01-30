import os
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
    codespace = os.environ.get("CODESPACE_NAME")
 
    if codespace:
        base_url = f"https://{codespace}-8000.app.github.dev"
    else:
        base_url = "http://localhost:8000"
 
    return Response({
        "users": f"{base_url}/api/users/",
        "teams": f"{base_url}/api/teams/",
        "activities": f"{base_url}/api/activities/",
        "workouts": f"{base_url}/api/workouts/",
        "leaderboard": f"{base_url}/api/leaderboard/",
    })
 
 
urlpatterns = [
    path("", api_root),
    path("api/", include(router.urls)),
    path("admin/", admin.site.urls),
]