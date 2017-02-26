from django.conf.urls import url

from Art_Sign.agenda.views import EventListView, EventCreate, EventDelete

urlpatterns = [
    url(r'^$', EventListView.as_view(), name='event-list'),
    url(r'^new/$', EventCreate.as_view(), name='event-create'),
    url(r'^delete/(?P<pk>[0-9]+)/$', EventDelete.as_view(),
        name='event-delete'),
]
