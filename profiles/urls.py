from django.urls import path

from rest_framework import routers

from profiles.views import DashboardAPIView

app_name = "profiles"

router = routers.SimpleRouter()


urlpatterns = [
    path("dashboard/", DashboardAPIView.as_view(), name="dashboard"),
] + router.urls
