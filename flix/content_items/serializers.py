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
        depth = 1

class SeriesSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Series
        depth = 1

class EpisodeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Episode
        depth = 2
