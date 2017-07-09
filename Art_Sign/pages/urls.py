from django.conf.urls import url

from Art_Sign.pages.views import about, outings

urlpatterns = [
    url(r'^apropos/$', about, name='about'),
    url(r'^sorties/$', outings, name='outings'),
]
