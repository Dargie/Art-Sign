from django.conf.urls import url

from Art_Sign.agenda.api.views import EventListAPI, EventDetailAPI

urlpatterns = [
    url(r'^$', EventListAPI.as_view(), name='list'),
    url(r'^(?P<event_id>[0-9]+)/?$', EventDetailAPI.as_view(), name='detail'),
]
