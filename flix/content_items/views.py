# External
from rest_framework import filters, viewsets

# Local
from .filters import MovieFilter, SeriesFilter, EpisodeFilter
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
    filter_class = MovieFilter

class SeriesViewSet(viewsets.ModelViewSet):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    filter_class = SeriesFilter

class EpisodeViewSet(viewsets.ModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer
    filter_class = EpisodeFilter
