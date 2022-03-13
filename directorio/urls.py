from django.urls import path, include
from .views import UserViewSet, ChangePasswordView, SignupView, LoginView
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

router = routers.DefaultRouter()

router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    # path('login/', LoginView.as_view(), name='auth_login'),
    path('signup/', SignupView.as_view(), name='auth_signup'),
    path('change_password/', ChangePasswordView.as_view(), name='auth_chpass'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/verify/', TokenVerifyView.as_view(), name='token_verify'),
]