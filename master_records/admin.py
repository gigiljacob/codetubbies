from django.contrib import admin

from master_records.models import (Skill, Degree, JobRole, TestTopic, EventCategory)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    fields = ("skill", )


@admin.register(Degree)
class DegreeAdmin(admin.ModelAdmin):
    fields = ("degree", )


@admin.register(JobRole)
class JobRoleAdmin(admin.ModelAdmin):
    fields = ("job_role", )


@admin.register(TestTopic)
class TestTopicAdmin(admin.ModelAdmin):
    fields = ("topic", )


@admin.register(EventCategory)
class EventCategoryAdmin(admin.ModelAdmin):
    fields = ("name", )
