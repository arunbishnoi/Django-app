from django.conf.urls import patterns, include, url
from django.contrib import admin
from result.views import *

urlpatterns = patterns('',  
    url(r'^display/', display),
    url(r'^marks/',  marks),
    url(r'^admin/', include(admin.site.urls)),
)
