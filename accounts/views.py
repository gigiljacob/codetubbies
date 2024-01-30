from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from accounts.serializers import UserTokenObtainPairSerializer, RegisterSerializer


User = get_user_model()


class UserObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = UserTokenObtainPairSerializer

    def post(self, request):
        response = super().post(self.request)

        return Response({"result": response.data}, status=response.status_code)


class UserTokenRefreshView(TokenRefreshView):

    def post(self, request: Request, *args, **kwargs) -> Response:
        response = super().post(request)
        return Response({"result": response.data}, status=response.status_code)


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request)
        return Response({"result": response.data}, status=response.status_code)
