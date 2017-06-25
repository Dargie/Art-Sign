from django.views.generic.list import ListView

from Art_Sign.agenda.models import Event


class EventListView(ListView):

    model = Event

