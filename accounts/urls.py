from django.conf.urls import patterns, url, include

from accounts.views import *

urlpatterns = patterns('',
    # Companies
    url(r'^users/$', Users.as_view(), name='users'),
    url(r'^users/(?P<pk>\d+)/promote/$', promote, name='promote'),
    url(r'^users/(?P<pk>\d+)/demote/$', demote, name='demote'),
    url(r'^add_user/$', AddUser.as_view(), name='add_user'),
    url(r'^users/(?P<pk>\d+)/$', DeleteUser.as_view(), name='delete_user'),
    url(r'^update_profile/$', ProfileUpdate.as_view(), name='update_profile'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    'authtools.views.password_reset_confirm_and_login',
    name='password_reset_confirm'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
)
