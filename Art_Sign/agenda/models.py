from datetime import datetime

from django.db import models


class Event(models.Model):
    """
    Model Event
    title: title of the event
    description: description of the event
    place: place of the event
    date: date of the event
    """
    class Meta:
        verbose_name = "Événement"
        verbose_name_plural = "Événements"

    title = models.CharField(max_length=80, verbose_name="Nom de l'événement")
    date = models.DateTimeField(verbose_name="Date")
    place = models.CharField(max_length=80, blank=True, verbose_name="Lieu")
    description = models.CharField(max_length=200, blank=True,
                                   verbose_name="Description")

    def __str__(self):
        return self.title

    def is_past(self):
        """
        Test if the event's date is past.
        :return: True id the event's date is past, False if it's not.
        :rtype: bool
        """
        if self.date > datetime.now():
            return True
        elif self.date < datetime.now():
            return False
