from datetime import UTC

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.datetime_safe import datetime

User = get_user_model()


class CodeTubbiesBaseModel(models.Model):
    user = models.ForeignKey(User, models.CASCADE, verbose_name="Created by", null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True, auto_created=True)
    updated_at = models.DateTimeField(auto_now_add=True, auto_created=True)

    class Meta:
        abstract = True


class ProfileBaseModel(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    created_at = models.DateTimeField(auto_now=True, auto_created=True)
    updated_at = models.DateTimeField(auto_now_add=True, auto_created=True)

    class Meta:
        abstract = True


class Skill(models.Model):
    skill = models.CharField(max_length=50)

    def __str__(self):
        return self.skill


class Degree(models.Model):
    degree = models.CharField(max_length=100)

    def __str__(self):
        return self.degree


class JobRole(models.Model):
    job_role = models.CharField(max_length=100)

    def __str__(self):
        return self.job_role


class TestTopic(models.Model):
    topic = models.CharField(max_length=50)

    def __str__(self):
        return self.topic


class EventCategory(models.Model):
    name = models.CharField(max_length=100)
