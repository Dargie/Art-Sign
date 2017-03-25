from rest_framework.generics import ListAPIView, RetrieveAPIView

from Art_Sign.article.api.serializers import ArticleListSerializer, ArticleDetailSerializer
from Art_Sign.article.models import Article


class ArticleListAPI(ListAPIView):

    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer


class ArticleDetailAPI(RetrieveAPIView):

    queryset = Article.objects.all()
    lookup_url_kwarg = 'article_id'
    serializer_class = ArticleDetailSerializer
