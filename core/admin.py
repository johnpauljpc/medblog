from django.contrib import admin
from .models import Article, articleSeries, subscriberedUsers


class seriesModel(admin.ModelAdmin):
     list_display = ['title', 'subtitle' ,'author', 'published']
     fieldsets = (
          ('header', {'fields':['title', 'subtitle', 'image', 'slug']}),
          ('date', {'fields': ['published']})
     )
     prepopulated_fields = {'slug': ['title']}

class articleModel(admin.ModelAdmin):
     list_display = [ 'title',  'subtitle','author', 'published', 'modified']

     fieldsets = (
          ('head', {'fields': ['title', 'subtitle', 'series','image', 'author']}),
          ('body', {'fields': ['article_slug','content', 'note']}),
          ('date', {'fields': ['published', 'modified']})
     )
     prepopulated_fields = {'article_slug': ('title',)}

class subscribers_adminForm(admin.ModelAdmin):
     list_display = ('name', 'email', 'created_date', )
     

# Register your models here.
# admin.site.register(Author)
admin.site.register(articleSeries, seriesModel)
admin.site.register(Article, articleModel)
admin.site.register(subscriberedUsers, subscribers_adminForm)
