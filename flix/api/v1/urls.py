# Django
from django.conf.urls import include, url

# Local
from flix.account.urls import router as account_router
from flix.django_auth.urls import router as django_auth_router

urlpatterns = [
    url(r'', include(django_auth_router.urls)), 
    url(r'^account/', include(account_router.urls))
]
