from django.conf.urls import url

from . import views

app_name = 'anime'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<title>[\s\S]+)/$', views.detail, name='detail')
]
