from django.conf.urls import url
#from django.contrib import admin
from . import views

app_name = 'rapidamente'

urlpatterns = [
    url(r'^(?P<slug>[A-Z0-9]+)/$', views.ShortUrlDetailView.as_view(), name='detail'),
    url(r'^hello$', views.ShortUrlCreateView.as_view(), name='index'),
]
