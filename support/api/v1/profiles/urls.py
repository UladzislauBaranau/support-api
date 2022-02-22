from django.urls import path

from .views import ListProfilesView, UpdateSupportStatusView

urlpatterns = [
    path('all/', ListProfilesView.as_view()),
    path('update-support/<int:pk>/', UpdateSupportStatusView.as_view()),
]
