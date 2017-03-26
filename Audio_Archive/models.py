from __future__ import unicode_literals

# Create your models here.
from django.db import models

from taggit.managers import TaggableManager

# the following lines added:
import datetime
import calendar
from django.utils import timezone

class Speaker(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Conference(models.Model):
    year = models.IntegerField()
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Day(models.Model):
    date = models.DateField()
    conference = models.ForeignKey(Conference)

    def __str__(self):
        return self.date.strftime("%a %d %b")

class TimeSlot(models.Model):
    time = models.TimeField()
    day = models.ForeignKey(Day)

    def __str__(self):
        return self.day.__str__() + "|" + self.time.strftime("%H:%M")

    def gettime(self):
        return self.time.strftime("%H:%M")

class Talk(models.Model):
    title = models.CharField(max_length=400)
    speaker = models.ForeignKey(Speaker, null=True, blank=True)
    category = models.ForeignKey(Category, null=True, blank=True)
    timeslot = models.ForeignKey(TimeSlot)

    publish = models.BooleanField
    publish_after = models.DateField('publish_after', null=True, blank=True)
    audio_file = models.FileField(upload_to='media/talks', null=True, blank=True)
    short_description = models.CharField(max_length=300, blank=True)
    description = models.CharField(max_length=1000, blank=True)
    image = models.FileField(upload_to='media/images', null=True, blank=True)
    tags = TaggableManager()

    def __str__(self):
        return self.title