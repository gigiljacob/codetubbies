from django.contrib import admin

from events.models import (Speakers, Events, Participant)


@admin.register(Speakers)
class SpeakersAdmin(admin.ModelAdmin):
    fields = ("name", "designation")


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    fields = ("category", "topic", "start_on", "speakers")


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    fields = ("event", "user")
