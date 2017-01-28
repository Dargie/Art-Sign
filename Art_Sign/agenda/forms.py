from django.forms import ModelForm

from Art_Sign.agenda.models import Event


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'date', 'place', 'description']
