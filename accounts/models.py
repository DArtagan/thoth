from django.db import models
from authtools.models import AbstractNamedUser
from django.core.urlresolvers import reverse

class User(AbstractNamedUser):

    def username():
        return self.email

    class Meta:
        db_table = 'auth_user'

    def get_delete_url(self):
        return reverse('accounts:delete_user', args=[self.pk])

    def __unicode__(self):
        return self.name
