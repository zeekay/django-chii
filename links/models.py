from django.db import models
from utils.models import GetOrNoneManager
from taggit.managers import TaggableManager

class Link(models.Model):
    nick = models.CharField(max_length=50)
    host = models.CharField(max_length=100)
    channel = models.CharField(max_length=50)
    link = models.CharField(max_length=200)
    title = models.TextField(max_length=100, blank=True)
    context = models.TextField()
    added = models.DateTimeField()

    objects = GetOrNoneManager()

    tags = TaggableManager()

class Relink(models.Model):
    link = models.ForeignKey(Link)
