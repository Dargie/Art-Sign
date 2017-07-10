from django.conf.urls import url

from Art_Sign.pages.views import about, outings, achievements, services, participate

urlpatterns = [
    url(r'^apropos/$', about, name='about'),
    url(r'^sorties/$', outings, name='outings'),
    url(r'^realisations/$', achievements, name='achievements'),
    url(r'^services/$', services, name='services'),
    url(r'^participate/', participate, name='participate'),
]
