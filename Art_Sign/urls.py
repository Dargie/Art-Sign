from django.conf.urls import include, url
from django.contrib import admin

from Art_Sign.pages.views import home

urlpatterns = [
    url('^$', home, name='homepage'),

    url(r'^', include('Art_Sign.pages.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('Art_Sign.api.urls')),
    url(r'tinymce/', include('tinymce.urls')),
    url(r'^agenda/', include('Art_Sign.agenda.urls')),
    url(r'^article/', include('Art_Sign.article.urls')),
]
