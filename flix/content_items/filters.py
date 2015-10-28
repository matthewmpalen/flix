# External
import django_filters

# Local
from .models import Movie, Series, Episode

class MovieFilter(django_filters.FilterSet):
    tag = django_filters.CharFilter(name='tags__name')

    class Meta:
        model = Movie
        fields = ('tag',)

class SeriesFilter(django_filters.FilterSet):
    tag = django_filters.CharFilter(name='tags__name')

    class Meta:
        model = Series
        fields = ('tag',)

class EpisodeFilter(django_filters.FilterSet):
    tag = django_filters.CharFilter(name='series__tags__name')

    class Meta:
        model = Episode
        fields = ('tag',)

