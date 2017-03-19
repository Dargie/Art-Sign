from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from Art_Sign.agenda.models import Event


class EventSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'

    logo = serializers.CharField(source='get_relative_logo_url')


class EventDetailSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'

    logo = serializers.CharField(source='get_relative_logo_url')
