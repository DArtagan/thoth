from django.db import models

from authtools.models import AbstractNamedUser

class User(AbstractNamedUser):
    class Meta:
        db_table = 'auth_user'
