from django.conf.urls import url
#from django.contrib import admin
from . import views

app_name = 'rapidamente'

urlpatterns = [
    #url(r'^(?P<slug>[A-Z0-9]+)/$', views.ShortUrlDetailView.as_view(), name='detail'),
    url(r'^hello/$', views.hello, name='detail'),
    #url(r'^(?P<slug>[0-9A-Za-z-]+)/$', views.hello, name='detail_box'),
    url(r'^url/(?P<slug>[0-9A-Za-z-]+)/$', views.detail_box, name='detail_box'),
    #url(r'^$', views.homepage_and_create_shorturl, name='index'),
]
