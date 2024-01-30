from django.db import models

from master_records.models import (Degree, JobRole, ProfileBaseModel, Skill)


class Strength(ProfileBaseModel):
    role = models.CharField(max_length=50)
    skill = models.ManyToManyRel('skill', Skill,)


class LicensesCertification(models.Model):
    name = models.CharField(max_length=150)
    organization = models.CharField(max_length=100)
    expiry = models.BooleanField(default=False)
    issue_date = models.DateField()
    expiry_date = models.DateField()
    credentials_id = models.CharField(max_length=200)
    credentials_uri = models.URLField()

    def __str__(self):
        return self.name


class Experience(ProfileBaseModel):
    job_role = models.ForeignKey(JobRole, models.PROTECT)
    project = models.BooleanField(default=False)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    currently_working = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.job_role


class Education(ProfileBaseModel):
    institute_name = models.CharField(max_length=150)
    degree = models.ForeignKey(Degree, on_delete=models.PROTECT)
    course = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    marks = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.institute_name


class Profile(ProfileBaseModel):
    summary = models.TextField()
    resume = models.FileField(upload_to='media/resumes')

