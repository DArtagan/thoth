from django.db import models

from authtools.models import AbstractNamedUser, AbstractEmailUser

class User(AbstractNamedUser):
    def username():
        return self.email

    class Meta:
        db_table = 'auth_user'

    def __unicode__(self):
        return self.name
