from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('Art_Sign.pages.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('Art_Sign.api.urls')),
    url(r'^agenda/', include('Art_Sign.agenda.urls')),
]
