from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
from tinymce.models import HTMLField

class Template(models.Model):
    name = models.CharField(max_length=50)
    date_edited = models.DateField(auto_now=True)
    template = models.TextField()
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False)
    
    def get_absolute_url(self):
        return reverse('scribe:template:template_detail', args=[self.pk])

    def get_update_url(self):
        return reverse('scribe:template:template_update', args=[self.pk])

    def get_delete_url(self):
        return reverse('scribe:template:template_delete', args=[self.pk])

    def __unicode__(self):
        return self.name


class Header(models.Model):
    name = models.CharField(max_length=50)
    date_edited = models.DateField(auto_now=True)
    image = models.ImageField(upload_to='headers')
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False)
    
    def get_absolute_url(self):
        return reverse('scribe:header:header_detail', args=[self.pk])

    def get_update_url(self):
        return reverse('scribe:header:header_update', args=[self.pk])

    def get_delete_url(self):
        return reverse('scribe:header:header_delete', args=[self.pk])

    def __unicode__(self):
        return self.name


class Email(models.Model):
    name = models.CharField(max_length=100)
    date_edited = models.DateField(auto_now=True)
    template = models.ForeignKey(Template)
    header = models.ForeignKey(Header)
    content = HTMLField(blank=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False, related_name='creator')

    class Meta:
        permissions = (
            ('view_email', 'View Email'),
        )

    def get_absolute_url(self):
        return reverse('scribe:email:email_detail', args=[self.pk])

    def get_update_url(self):
        return reverse('scribe:email:email_update', args=[self.pk])

    def get_delete_url(self):
        return reverse('scribe:email:email_delete', args=[self.pk])

    def __unicode__(self):
        return self.name
