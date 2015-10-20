# Django
from django.contrib.auth.models import User, Group

# External
from rest_framework.serializers import HyperlinkedModelSerializer

# Local
from flix.account.models import ViewerProfile

class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'last_login', 'username', 'first_name', 'last_name', 
            'date_joined')
        read_only_fields = ('last_login', 'username', 'date_joined')

class GroupSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class UserViewerProfileSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ViewerProfile
        fields = ('name', 'is_child')


