from rest_framework.generics import ListAPIView

from Art_Sign.agenda.api.serializers import EventSerializer
from Art_Sign.agenda.models import Event


class EventListAPI(ListAPIView):

    queryset = Event.objects.all()
    serializer_class = EventSerializer
