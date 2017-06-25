from django.conf.urls import url

from Art_Sign.article.views import ArticleListView, ArticleDetailView

urlpatterns = [
    url(r'^$', ArticleListView.as_view(), name='article-list'),
    url(r'^(?P<pk>[-\w]+)/$', ArticleDetailView.as_view(), name='article-detail'),
]