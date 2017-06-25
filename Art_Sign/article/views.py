from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from Art_Sign.article.models import Article


class ArticleListView(ListView):

    model = Article


class ArticleDetailView(DetailView):

    model = Article
