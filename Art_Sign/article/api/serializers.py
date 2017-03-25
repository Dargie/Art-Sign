from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from Art_Sign.article.models import Article


class ArticleListSerializer(ModelSerializer):

    class Meta:
        model = Article
        exclude = ('content',)

    logo = serializers.CharField(source='get_relative_logo_url')


class ArticleDetailSerializer(ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'

    logo = serializers.CharField(source='get_relative_logo_url')
