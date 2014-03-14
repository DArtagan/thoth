from django.conf.urls import patterns, include, url
from scribe.views import * 

# Email
email = patterns('',
    url(r'^$', EmailIndex.as_view(), name='email_index'),
    url(r'^(?P<pk>\d+)/$', EmailDetail.as_view(), name='email_detail'),
    url(r'^create/$', EmailCreate.as_view(), name='email_create'),
    url(r'^(?P<pk>\d+)/update/$', EmailUpdate.as_view(), name='email_update'),
    url(r'^(?P<pk>\d+)/delete/$', EmailDelete.as_view(), name='email_delete'),
)

# Template
template = patterns('',
    url(r'^$', TemplateIndex.as_view(), name='template_index'),
    url(r'^(?P<pk>\d+)/$', TemplateDetail.as_view(), name='template_detail'),
    url(r'^create/$', TemplateCreate.as_view(), name='template_create'),
    url(r'^(?P<pk>\d+)/update/$', TemplateUpdate.as_view(), name='template_update'),
    url(r'^(?P<pk>\d+)/delete/$', TemplateDelete.as_view(), name='template_delete'),
    )

# Header
header = patterns('',
    url(r'^$', HeaderIndex.as_view(), name='header_index'),
    url(r'^(?P<pk>\d+)/$', HeaderDetail.as_view(), name='header_detail'),
    url(r'^create/$', HeaderCreate.as_view(), name='header_create'),
    url(r'^(?P<pk>\d+)/update/$', HeaderUpdate.as_view(), name='header_update'),
    url(r'^(?P<pk>\d+)/delete/$', HeaderDelete.as_view(), name='header_delete'),
)

urlpatterns = patterns('',
    url(r'^email/', include(email, namespace='email')),
    url(r'^template/', include(template, namespace='template')),
    url(r'^header/', include(header, namespace='header')),
    url(r'^upload/$', upload, name='upload_image'),
)
