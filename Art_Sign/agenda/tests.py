from django.test import TestCase

from Art_Sign.agenda.models import Event


class EventModelTest(TestCase):
    """
    Test the event model.
    """

    def test_string_representation(self):
        """
        Test the string representation of the event model.
        """
        event = Event(title="Assemblée générale !")
        self.assertEqual(str(event), event.title)
