from django.conf.urls import include, url

urlpatterns = [
    url(r'^agenda/', include('Art_Sign.agenda.api.urls'))
]
