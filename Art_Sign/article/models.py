from datetime import datetime

from django.db import models
from tinymce import models as tinymce_models


class Article(models.Model):
    """
    Model Article
    title: title of the content
    pub_date: date of the publication
    logo: logo of the article
    content: content of the article
    """
    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    title = models.CharField(max_length=200, verbose_name="Titre")
    pub_date = models.DateTimeField(blank=True, null=True, verbose_name="Date de publication")
    logo = models.ImageField(blank=True, upload_to="uploads")
    content = tinymce_models.HTMLField()

    def __str__(self):
        return self.title

    def is_public(self):
        """
        Test if the article is public.
        The article is public only if the publication date is past.
        :return: True if the article is public, False if it's not.
        :rtype: bool
        """
        if self.pub_date < datetime.now():
            return True
        elif self.pub_date > datetime.now():
            return False

    def get_relative_logo_url(self):
        """
        Get the relative URL of the logo.
        """
        if self.logo:
            relative_url = self.logo.name
        elif not self.logo:
            relative_url = None
        return relative_url
