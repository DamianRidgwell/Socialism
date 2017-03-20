from __future__ import unicode_literals

# Create your models here.
from django.db import models

from taggit.managers import TaggableManager

# the following lines added:
import datetime
from django.utils import timezone

class Speaker(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Talk(models.Model):
    title = models.CharField(max_length=400)
    speaker = models.ForeignKey(Speaker)
    category = models.ForeignKey(Category)
    publish = models.BooleanField
    publish_after = models.DateField('publish_after', null=True, blank=True)
    audio_file = models.FileField(upload_to='media/talks', null=True, blank=True)
    description = models.CharField(max_length=1000, blank=True)
    tags = TaggableManager()

    def __str__(self):
        return self.title