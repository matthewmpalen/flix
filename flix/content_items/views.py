# External
from rest_framework import viewsets

# Local
from .models import Person, Movie, Series, Episode
from .serializers import PersonSerializer, MovieSerializer
from .serializers import SeriesSerializer, EpisodeSerializer

###########
# Viewsets
###########

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SeriesViewSet(viewsets.ModelViewSet):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer

class EpisodeViewSet(viewsets.ModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer
