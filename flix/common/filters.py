# External
import django_filters

# Local
from .models import Tag

class TagFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(name='name', lookup_type='contains')

    class Meta:
        model = Tag
        fields = ('name',)
