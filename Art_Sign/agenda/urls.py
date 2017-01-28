from django.conf.urls import url

from Art_Sign.agenda.views import EventCreate

urlpatterns = [
    url(r'^new/$', EventCreate.as_view(), name='event-create'),
]

