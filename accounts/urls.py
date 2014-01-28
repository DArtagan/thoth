from django.conf.urls import patterns, url, include

from accounts.views import *

urlpatterns = patterns('',
    # Companies
    url(r'^update_email/$', EmailUpdate.as_view(), name='update_email'),
)
