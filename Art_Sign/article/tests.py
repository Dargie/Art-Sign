from django.test import TestCase

from Art_Sign.article.models import Article
from Art_Sign.article.factories import ArticleNotPublishedWithLogoFactory, ArticlePublishedAndWithoutLogoFactory
from Art_Sign import settings


class ArticleModelTest(TestCase):
    """
    Test the article model.
    """
    def setUp(self):

        self.article_not_published_with_logo = ArticleNotPublishedWithLogoFactory()
        self.article_published_and_without_logo = ArticlePublishedAndWithoutLogoFactory()

    def test_string_representation(self):
        """
        Test the string representation of the article model.
        """
        article = Article(title="Assemblée générale !")
        self.assertEqual(str(article), article.title)
        self.assertEqual(str(self.article_not_published_with_logo), self.article_not_published_with_logo.title)

    def test_is_public(self):
        """
        Test the is_public method.
        """
        self.assertEqual(self.article_published_and_without_logo.is_public(), True)

    def test_is_not_public(self):
        """
        Test the is_public method.
        """
        self.assertEqual(self.article_not_published_with_logo.is_public(), False)

    def test_get_relative_logo_url(self):
        """
        Test the get_relative_logo_url.
        """
        self.assertEqual(self.article_not_published_with_logo.logo, self.article_not_published_with_logo.get_relative_logo_url())

    def test_is_not_an_absolute_logo_url(self):
        """
        Test the get_relative_logo_url.
        """
        absolute_url = u'{0}/{1}'.format(settings.MEDIA_URL, self.article_not_published_with_logo.logo)
        self.assertNotEqual(absolute_url, self.article_not_published_with_logo.get_relative_logo_url())
