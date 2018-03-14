# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class ModelOne(models.Model):

    user = models.OneToOneField(User)

    profile_pic = models.ImageField(upload_to='pictures',blank=True)
    portfolio = models.URLField(blank=True)


    def __str__(self):
        return self.user.username
