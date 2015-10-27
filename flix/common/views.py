# External
from rest_framework import viewsets

# Local
from .models import Tag
from .serializers import TagSerializer

###########
# Viewsets
###########

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
