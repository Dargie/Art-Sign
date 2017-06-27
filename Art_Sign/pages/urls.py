from django.conf.urls import url

from Art_Sign.pages.views import about

urlpatterns = [
    url(r'^apropos/$', about, name='about')
]
