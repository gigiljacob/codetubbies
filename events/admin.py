from django.contrib import admin

from events.models import (Speaker, Event, Participant)


BASE_FIELDS = ("created_at", "updated_at", "user")


@admin.register(Speaker)
class SpeakersAdmin(admin.ModelAdmin):
    fields = ("name", "designation")
    list_display = fields + BASE_FIELDS


@admin.register(Event)
class EventsAdmin(admin.ModelAdmin):
    fields = ("category", "topic", "start_on", "speakers")
    list_display = fields + BASE_FIELDS


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    fields = ("event", "user")
