from datetime import datetime

from rest_framework.generics import ListAPIView, RetrieveAPIView

from Art_Sign.article.api.serializers import ArticleListSerializer, ArticleDetailSerializer
from Art_Sign.article.models import Article


class ArticleListAPI(ListAPIView):

    queryset = Article.objects.exclude(pub_date__gte=datetime.now())
    serializer_class = ArticleListSerializer


class ArticleDetailAPI(RetrieveAPIView):

    queryset = Article.objects.exclude(pub_date__gte=datetime.now())
    lookup_url_kwarg = 'article_id'
    serializer_class = ArticleDetailSerializer
