from django.conf.urls import url

from Art_Sign.agenda.views import EventListView, EventCreate

urlpatterns = [
    url(r'^', EventListView.as_view(), name='event-list'),
    url(r'^new/$', EventCreate.as_view(), name='event-create'),
]

