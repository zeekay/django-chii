from django.db import models

class GetOrNoneManager(models.Manager):
    """Adds get_or_none method to objects"""
    def get_or_none(self, **kwargs):
        try:
            return self.get(**kwargs)
        except self.model.DoesNotExist:
            return None

class Quote(models.Model):
    nick = models.CharField(max_length=50)
    host = models.CharField(max_length=100)
    channel = models.CharField(max_length=50)
    quote = models.TextField()
    added = models.DateField()

    objects = GetOrNoneManager()
