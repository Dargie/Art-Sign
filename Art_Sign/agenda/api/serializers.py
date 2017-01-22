from rest_framework.serializers import ModelSerializer

from Art_Sign.agenda.models import Event


class EventSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'


class EventDetailSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'
