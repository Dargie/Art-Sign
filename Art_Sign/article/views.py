import datetime

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from Art_Sign.article.models import Article


class ArticleListView(ListView):

    model = Article

    def get_queryset(self):
        today = datetime.date.today()
        return Article.objects.exclude(pub_date__gte=today)


class ArticleDetailView(DetailView):

    model = Article
