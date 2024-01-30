from django.contrib import admin

from practice.models import (Factor, Discussion, Question, Submission)


@admin.register(Factor)
class FactorAdmin(admin.ModelAdmin):
    fields = ("category", "topics")


@admin.register(Discussion)
class DiscussionAdmin(admin.ModelAdmin):
    fields = ("comments", )


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = ("factor", "problem", "discussion")


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    fields = ("submitted_by", "problem", "solution")
