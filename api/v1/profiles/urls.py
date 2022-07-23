from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .views import ListProfilesView, UpdateSupportStatusView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh-token/', TokenRefreshView.as_view()),
    path('token-verify/', TokenVerifyView.as_view()),

    path('all/', ListProfilesView.as_view()),
    path('update-support/<int:pk>/', UpdateSupportStatusView.as_view()),
]
