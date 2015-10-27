# Django
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.db import models

class ViewerProfile(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=10)
    is_child = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (
            ('user', 'name')
        )

    def __str__(self):
        return '{0}: {1}'.format(self.user.username, self.name)

class ViewEvent(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    viewed_object = GenericForeignKey('content_type', 'object_id')
    viewer_profile = models.ForeignKey(ViewerProfile)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.viewed_object.__str__()
