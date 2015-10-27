# External
from rest_framework import routers

# Local
from .views import ViewerProfileViewSet, ViewEventViewSet

router = routers.SimpleRouter()
router.register(r'viewer_profiles', ViewerProfileViewSet)
router.register(r'view_events', ViewEventViewSet)
