from django.conf.urls import patterns, url, include

from accounts.views import *

urlpatterns = patterns('',
    # Companies
    url(r'^add_user/$', AddUser.as_view(), name='add_user'),
    url(r'^update_email/$', EmailUpdate.as_view(), name='update_email'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    'authtools.views.password_reset_confirm_and_login',
    name='password_reset_confirm'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
)
