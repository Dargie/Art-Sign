from datetime import datetime, timedelta
import factory

from django.db.models import ImageField

from Art_Sign.article.models import Article


class ArticleNotPublishedWithLogoFactory(factory.DjangoModelFactory):

    class Meta:
        model = Article

    title = "Assemblée générale"
    pub_date = datetime.now() + timedelta(days=7)
    logo = factory.django.ImageField(filename='logo.jpg')

class ArticlePublishedAndWithoutLogoFactory(factory.DjangoModelFactory):

    class Meta:
        model = Article

    title = "Assemblée générale"
    pub_date = datetime.now() - timedelta(days=7)
