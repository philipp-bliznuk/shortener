# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Url(models.Model):
    origin = models.URLField(max_length=255)
    hash = models.CharField(max_length=255, unique=True)

    def __unicode__(self):
        return 'Link to {self.origin} ({self.hash})'.format(self=self)
