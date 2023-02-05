from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Author(models.Model):
    pass

class articleSeries(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    slug = models.SlugField('Series slug', unique=True)
    publised = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Series"
        #ordering = ['-published']
    

class Article(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200, default="no subtittle", blank=True, null=True)
    article_slug = models.SlugField('Article slug', unique=True)
    content = models.TextField()
    published = models.DateTimeField('publised date', auto_now_add=True)
    modified = models.DateTimeField('modified date', auto_now=True)
    series = models.ForeignKey(articleSeries, default="", on_delete=models.SET_DEFAULT)
    # author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    @property
    def slug(self):
        return slug.article_slug

    class Meta:
        pass




