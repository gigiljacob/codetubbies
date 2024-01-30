from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class DashboardSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "i_am", "name", "email", "gender", "company",
                  "skills", "is_active", )
