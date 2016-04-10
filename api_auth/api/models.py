from __future__ import unicode_literals
from django.utils.encoding import smart_unicode
from django.db import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    token = models.CharField(max_length=180)
    is_new = models.CharField(default=True,max_length=10)
    ACCOUNT_USERNAME_REQUIRED = False

    def __unicode__(self):
        return smart_unicode(self.is_new)

