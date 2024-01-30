from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from profiles.models import Profile
from profiles.serializers import DashboardSerializer

User = get_user_model()


class DashboardAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = DashboardSerializer(request.user)
        return Response({"result": serializer.data}, status=status.HTTP_200_OK)


class ProfileAPIView(RetrieveUpdateAPIView):
    model = Profile

    def get_queryset(self):
        # active_user =
        # qs = self.model.objects.get(user=)
        pass
