from django.conf.urls import url
#from django.contrib import admin
from . import views

app_name = 'rapidamente'

urlpatterns = [
    #About Us
    url(r'^about/$', views.AboutUsTemplateView.as_view(), name='about'),
    #Create a url shortened POST+GET
    url(r'^myurl/$', views.homepage_and_create_shorturl, name='create'),
    #View the URL link
    url(r'^url/(?P<slug>[0-9A-Za-z-]+)/$', views.detail_box, name='detail'),

]
