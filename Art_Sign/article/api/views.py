from datetime import datetime

from rest_framework.generics import ListAPIView, RetrieveAPIView

from Art_Sign.article.api.serializers import ArticleListSerializer, ArticleDetailSerializer
from Art_Sign.article.models import Article


class ArticleListAPI(ListAPIView):

    serializer_class = ArticleListSerializer

    def get_queryset(self):
        queryset = Article.objects.exclude(pub_date__gte=datetime.now())
        category = self.request.query_params.get('category', None)

        if category is not None:
            queryset = queryset.filter(category=category)

        return queryset


class ArticleDetailAPI(RetrieveAPIView):

    queryset = Article.objects.exclude(pub_date__gte=datetime.now())
    lookup_url_kwarg = 'article_id'
    serializer_class = ArticleDetailSerializer
