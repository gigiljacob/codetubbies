from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenVerifyView

from accounts.views import UserObtainTokenPairView, UserTokenRefreshView, RegisterView

app_name = "accounts"

router = DefaultRouter()

urlpatterns = [
    path('auth-token/', UserObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('auth-token/refresh/', UserTokenRefreshView.as_view(), name='token_refresh'),
    path('auth-token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('register/', RegisterView.as_view(), name='auth_register'),
]
