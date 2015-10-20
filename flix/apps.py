# Django
from django.apps import AppConfig

class FlixAppConfig(AppConfig):
    name = 'flix'

    def ready(self):
        import flix.django_auth.receivers
