from django.conf.urls import include, url

urlpatterns = [
    url(r'^agenda/', include('Art_Sign.agenda.api.urls')),
    url(r'^article/', include('Art_Sign.article.api.urls')),
    url(r'^documentation/', include('rest_framework_docs.urls')),
]
