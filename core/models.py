from django.db import models
from django.contrib.auth.models import User
# from django.utils import timezone
from django.utils import timezone
from tinymce.models import HTMLField
from django.contrib.auth import get_user_model

# Create your models here.
# class Author(models.Model):
#     author = models.ForeignKey(CustomUser, on_delete=models.CASCADE) 

class articleSeries(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    slug = models.SlugField('Series slug', unique=True)
    published = models.DateTimeField('Date published', default=timezone.now)
    author = models.ForeignKey(get_user_model(), default=8, on_delete = models.SET_DEFAULT) 

    class Meta:
        verbose_name_plural = "Series"
        #ordering = ['-published']

    def __str__(self):
        return self.title
    

class Article(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200, default="no subtittle", blank=True, null=True)
    article_slug = models.SlugField('Article slug', unique=True)
    content = HTMLField(blank = True, null= True, default="no content yet")
    note = HTMLField(blank = True, null= True, default="no note yet")
    published = models.DateTimeField('publised date',  default=timezone.now)
    modified = models.DateTimeField('modified date',  default=timezone.now)
    series = models.ForeignKey(articleSeries, default="", on_delete=models.SET_DEFAULT)
    author = models.ForeignKey(get_user_model(), default=8, on_delete = models.SET_DEFAULT) 


    @property
    def slug(self):
        return self.series.slug + "/" + self.article_slug
    
    def __str__(self):
        return self.title

    

    class Meta:
        pass




