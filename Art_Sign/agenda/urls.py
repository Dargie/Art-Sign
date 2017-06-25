from django.conf.urls import url

from Art_Sign.agenda.views import EventListView, EventDetailView

urlpatterns = [
    url(r'^$', EventListView.as_view(), name='event-list'),
    url(r'^(?P<pk>[-\w]+)/$', EventDetailView.as_view(), name='event-detail'),
]