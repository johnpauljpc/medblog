from django import forms
from .models import articleSeries, Article

class articleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title' ,'subtitle' ,'article_slug' ,'content' ,'series','image']
        

class seriesForm(forms.ModelForm):
    
    
    class Meta:
        model = articleSeries
        fields = ['title' ,'subtitle' ,'slug', 'image']


class SeriesUpdateForm(forms.ModelForm):
    class Meta:
        model = articleSeries

        fields = [
            "title",
            "subtitle",
            "image",
        ]

class ArticleUpdateForm(forms.ModelForm):
    class Meta:
        model = Article

        fields = [
            "title",
            "subtitle",
            "content",
            
            "series",
            "image",
        ]
        