from django.conf.urls import url, include
from django.contrib.auth.views import logout

urlpatterns = [
    url(r'^twitter', include('social_django.urls', namespace='social')),
    url(r'^logout', logout, name='logout'),
]
