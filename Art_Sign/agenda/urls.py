from django.conf.urls import url

from Art_Sign.agenda.views import EventListView

urlpatterns = [
    url(r'^$', EventListView.as_view(), name='event-list'),
]