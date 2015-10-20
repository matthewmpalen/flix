# External
from rest_framework import permissions

# Local
from .models import ViewerProfile

class ViewerProfilePermissions(permissions.DjangoModelPermissions):
    MAX_VIEWER_PROFILES = 5

    def has_permission(self, request, view):
        validated = super().has_permission(request, view)
        if not validated:
            return False

        if view.action == 'create':
            profile_count = ViewerProfile.objects.filter(
                user=request.user).count()
            if profile_count >= ViewerProfilePermissions.MAX_VIEWER_PROFILES:
                return False

        return True

    def has_object_permission(self, request, view, obj):
        validated = super().has_object_permission(request, view, obj)
        if not validated:
            return False

        return obj.user == request.user

class ViewEventPermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        if view.action == 'create' or view.action == 'destroy':
            return False
        elif view.action == 'list':
            return True

        return super().has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        validated = super().has_object_permission(request, view, obj)
        if not validated:
            return False

        return obj.user == request.user
