from django.conf.urls import url

from Art_Sign.article.api.views import ArticleListAPI, ArticleDetailAPI

urlpatterns = [
    url(r'^$', ArticleListAPI.as_view(), name='list'),
    url(r'^(?P<article_id>[0-9]+)/?$', ArticleDetailAPI.as_view(), name='detail'),
]