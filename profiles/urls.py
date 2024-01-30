from django.urls import path

from profiles.views import Dashboard

app_name = "profiles"

urlpatterns = [
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
]
