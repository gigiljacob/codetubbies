from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from profiles.models import Profile


User = get_user_model()


class Dashboard(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        return Response({"data": "success"})


class ProfileAPIView(RetrieveUpdateAPIView):
    model = Profile

    def get_queryset(self):
        # active_user =
        # qs = self.model.objects.get(user=)
        pass
