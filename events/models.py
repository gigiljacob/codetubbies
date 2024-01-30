from django.contrib.auth import get_user_model
from django.db import models

from master_records.models import EventCategory, CodeTubbiesBaseModel


class Speaker(CodeTubbiesBaseModel):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Event(CodeTubbiesBaseModel):
    category = models.ForeignKey(EventCategory, on_delete=models.PROTECT)
    topic = models.CharField(max_length=200)
    start_on = models.DateTimeField()
    speakers = models.ManyToOneRel("speakers", Speaker, "name")

    def __str__(self):
        return self.topic


class Participant(CodeTubbiesBaseModel):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
