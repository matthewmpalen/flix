# External
from rest_framework.serializers import HyperlinkedModelSerializer

# Local
from .models import Person, Movie, Series, Episode

class PersonSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Person

class MovieSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Movie

class SeriesSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Series

class EpisodeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Episode
