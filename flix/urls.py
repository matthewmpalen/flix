# Django
from django.conf.urls import include, url
from django.contrib import admin

# Local
from .views import HomepageView

urlpatterns = [
    url(r'^$', HomepageView.as_view(), name='home'), 
    url(r'^admin/', include(admin.site.urls)), 
    url(r'^api-auth/', include('rest_framework.urls', 
        namespace='rest_framework')), 
    url(r'^api/v1/', include('flix.api.v1.urls')), 
]
