from django.test import TestCase

from Art_Sign.agenda.factories import EventFactory
from Art_Sign.agenda.models import Event


class EventModelTest(TestCase):
    """
    Test the event model.
    """
    def setUp(self):

        self.event = EventFactory()

    def test_string_representation(self):
        """
        Test the string representation of the event model.
        """
        event = Event(title="Assemblée générale !")
        self.assertEqual(str(event), event.title)
        self.assertEqual(str(self.event), self.event.title)

    def test_is_past(self):
        """
        Test the is_past method.
        """
        self.assertEqual(self.event.is_past(), False)
