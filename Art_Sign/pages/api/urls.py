from django.conf.urls import url

from Art_Sign.pages.api.views import HomeAPIView

urlpatterns = [
    url(r'^', HomeAPIView.as_view(), name='home'),
]
