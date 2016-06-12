from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls import url, include, handler404, handler500


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('rapidamente.urls', namespace="rapidamente")),
]

handler404 = 'rapidamente.views.handler404'
handler500 = 'rapidamente.views.handler500'
