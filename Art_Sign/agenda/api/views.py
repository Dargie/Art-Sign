from rest_framework.generics import ListAPIView, RetrieveAPIView

from Art_Sign.agenda.api.serializers import \
 EventSerializer, EventDetailSerializer
from Art_Sign.agenda.models import Event


class EventListAPI(ListAPIView):

    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventDetailAPI(RetrieveAPIView):

    queryset = Event.objects.all()
    lookup_url_kwarg = 'event_id'
    serializer_class = EventDetailSerializer
