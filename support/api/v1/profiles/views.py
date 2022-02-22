from profiles.models import Profile

from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .serializers import ProfileSerializer, UpdateSupportStatusSerializer


class ListProfilesView(generics.ListCreateAPIView):
    """List of all user profiles."""
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class UpdateSupportStatusView(generics.RetrieveUpdateDestroyAPIView):
    """Admin sets the support status."""
    queryset = Profile.objects.all()
    serializer_class = UpdateSupportStatusSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
