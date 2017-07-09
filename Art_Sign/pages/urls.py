from django.conf.urls import url

from Art_Sign.pages.views import about, outings, achievements, services

urlpatterns = [
    url(r'^apropos/$', about, name='about'),
    url(r'^sorties/$', outings, name='outings'),
    url(r'^realisations/$', achievements, name='achievements'),
    url(r'^services/$', services, name='services'),
]
