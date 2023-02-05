from django.contrib import admin
from .models import Article, Author, articleSeries
from .model2 import student



# Register your models here.
admin.site.register(Author)
admin.site.register(articleSeries)
admin.site.register(Article)
admin.site.register(student)