from django.urls import include, path

urlpatterns = [
    path('profiles/', include('api.v1.profiles.urls')),
    path('tickets/', include('api.v1.tickets.urls')),
]
