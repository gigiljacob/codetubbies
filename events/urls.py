from django.urls import path

from rest_framework import routers

from events.views import EventCreateAPIView

app_name = "events"

router = routers.SimpleRouter()

urlpatterns = [
    path("event/", EventCreateAPIView.as_view(), name="create event"),
] + router.urls
