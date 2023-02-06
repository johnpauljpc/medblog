from django.contrib import admin
from .models import Article, articleSeries


class seriesModel(admin.ModelAdmin):
     list_display = ['title', 'subtitle' ,'slug', 'published']
     fieldsets = (
          ('header', {'fields':['title', 'subtitle', 'slug']}),
          ('date', {'fields': ['published']})
     )
     prepopulated_fields = {'slug': ['title']}

class articleModel(admin.ModelAdmin):
     list_display = [ 'title',  'subtitle','article_slug', 'published', 'modified']

     fieldsets = (
          ('head', {'fields': ['title', 'subtitle', 'series']}),
          ('body', {'fields': ['article_slug','content', 'note']}),
          ('date', {'fields': ['published', 'modified']})
     )
     prepopulated_fields = {'article_slug': ('title',)}
     

# Register your models here.
# admin.site.register(Author)
admin.site.register(articleSeries, seriesModel)
admin.site.register(Article, articleModel)
