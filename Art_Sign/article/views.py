import datetime

from django.core.exceptions import PermissionDenied
from django.utils import timezone
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

    def get_object(self, *args, **kwargs):
        now = timezone.now()
        article = super(ArticleDetailView, self).get_object(*args, **kwargs)
        if article.pub_date > now:
            raise PermissionDenied()
        else:
            return article
