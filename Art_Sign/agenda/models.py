from django.db import models


class Event(models.Model):

    title = models.CharField(max_length=80)

    date = models.DateTimeField()

    place = models.CharField(max_length=80, blank=True)

    description = models.CharField(max_length=200)
