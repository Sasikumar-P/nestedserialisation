# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class UnivStudent(models.Model):
    user = models.OneToOneField(User)
    subject_major = models.CharField(name="subject_major", max_length=60)
