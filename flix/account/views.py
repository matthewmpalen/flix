# Django

# External
from rest_framework import viewsets

# Local
from .models import ViewerProfile, ViewEvent
from .permissions import ViewerProfilePermissions, ViewEventPermissions
from .serializers import ViewerProfileSerializer, ViewEventSerializer

###########
# Viewsets
###########

class ViewerProfileViewSet(viewsets.ModelViewSet):
    queryset = ViewerProfile.objects.all()
    serializer_class = ViewerProfileSerializer
    permission_classes = (ViewerProfilePermissions,)

    def get_queryset(self):
        return ViewerProfile.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        instance = serializer.save(user=self.request.user)

class ViewEventViewSet(viewsets.ModelViewSet):
    queryset = ViewEvent.objects.all()
    serializer_class = ViewEventSerializer
    permission_classes = (ViewEventPermissions,)

    def get_queryset(self):
        viewer_profiles = ViewerProfile.objects.filter(user=self.request.user)
        return ViewEvent.objects.filter(viewer_profile__in=viewer_profiles)
