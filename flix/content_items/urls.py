# External
from rest_framework import routers

# Local
from .views import PersonViewSet, MovieViewSet, SeriesViewSet, EpisodeViewSet

router = routers.SimpleRouter()
router.register(r'people', PersonViewSet)
router.register(r'movies', MovieViewSet)
router.register(r'series', SeriesViewSet)
router.register(r'episodes', EpisodeViewSet)
