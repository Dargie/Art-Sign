from django.conf.urls import url

from Art_Sign.agenda.api.views import EventListAPI

urlpatterns = [
    url(r'^$', EventListAPI.as_view(), name='list')
]
