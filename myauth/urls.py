from django.conf.urls import url, include
from django.contrib.auth.views import logout

app_name = 'myauth'
urlpatterns = [
    url(r'^logout', logout, name='logout'),
]
