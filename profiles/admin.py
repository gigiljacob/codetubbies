from django.contrib import admin

from profiles.models import (Strength, LicensesCertification, Experience, Education, Profile)


@admin.register(Strength)
class StrengthAdmin(admin.ModelAdmin):
    fields = ("role", "skill")


@admin.register(LicensesCertification)
class LicensesCertificationAdmin(admin.ModelAdmin):
    fields = ("name", "organization", "expiry", "issue_date", "expiry_date",
              "credentials_id", "credentials_uri")


@admin.register(Experience)
class ExperienceCertificationAdmin(admin.ModelAdmin):
    fields = ("job_role", "project", "company", "location", "start_date",
              "end_date", "currently_working", "description")


@admin.register(Education)
class EducationCertificationAdmin(admin.ModelAdmin):
    fields = ("institute_name", "degree", "course", "start_date", "end_date",
              "marks")


@admin.register(Profile)
class ProfileCertificationAdmin(admin.ModelAdmin):
    fields = ("summary", "resume")
