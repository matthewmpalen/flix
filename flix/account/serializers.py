# Django

# External
from rest_framework.serializers import HyperlinkedModelSerializer

# Local
from .models import ViewerProfile, ViewEvent

class ViewerProfileSerializer(HyperlinkedModelSerializer):
    MAX_VIEWER_PROFILES = 5

    class Meta:
        model = ViewerProfile
        fields = ('url', 'name', 'is_child')

class ViewEventSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ViewEvent
        fields = ('url', 'viewer_profile')
