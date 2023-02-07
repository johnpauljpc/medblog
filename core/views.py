from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Article, articleSeries


# Create your views here.


def index(request):
    series = articleSeries.objects.all()
    context = {'series': series}
    return render(request, 'core/index.html', context)

def series(request, series):
    series = Article.objects.filter(series__slug = series).all()
    context = {'series': series}
    return render(request, 'core/index.html', context)



def article(request, series, article):
    article = Article.objects.filter(series__slug=series, article_slug=article).first()

    return render(request, 'core/articles.html', {'article':article})








'''
from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, ArticleSeries



def series(request, series: str):
    matching_series = Article.objects.filter(series__slug=series).all()
    
    return render(
        request=request,
        template_name='main/home.html',
        context={"objects": matching_series}
        )

def article(request, series: str, article: str):
    matching_article = Article.objects.filter(series__slug=series, article_slug=article).first()
    
    return render(
        request=request,
        template_name='main/article.html',
        context={"object": matching_article}
        )
'''