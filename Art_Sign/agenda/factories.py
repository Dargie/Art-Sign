from datetime import datetime, timedelta
import factory

from Art_Sign.agenda.models import Event


class EventFactory(factory.DjangoModelFactory):

    class Meta:
        model = Event

    title = "Assemblée générale"
    date = datetime.now() + timedelta(days=7)
    place = "Paris"
    description = "Dans une semaine, se tiendra l'assemblée générale de l'association."

