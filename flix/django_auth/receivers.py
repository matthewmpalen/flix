# Django
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Local
from flix.account.models import ViewerProfile

@receiver(post_save, sender=User)
def on_user_saved(sender, **kwargs):
    user = kwargs['instance']

    if kwargs.get('created', False):
        viewer_profile, created = ViewerProfile.objects.get_or_create(
            user=user, name='default', is_child=False 
        )
