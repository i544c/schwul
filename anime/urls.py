from django.conf.urls import url

from . import views

app_name = 'anime'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.add, name='add'),
    url(r'^(?P<title>[^\/]+)/$', views.detail, name='detail'),
    url(r'^(?P<title>[^\/]+)/edit/$', views.edit, name='edit'),
]
