from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Article, articleSeries
from .forms import articleForm, seriesForm, SeriesUpdateForm, ArticleUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from .decorators import check_if_user_is_superuser
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    series = articleSeries.objects.all()
    context = {'series': series,
               'type':'s'
               
               }
    return render(request, 'core/index.html', context)

def series(request, series):
    series = Article.objects.filter(series__slug = series).all()
    context = {'series': series,
               'type':'a'}
    return render(request, 'core/index.html', context)



def article(request, series, article):
    article = Article.objects.filter(series__slug=series, article_slug=article).first()

    return render(request, 'core/articles.html', {'article':article})

@check_if_user_is_superuser
def create_series(request):
    if request.method == 'POST':
        form = seriesForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.info(request, 'a new series has been created')
            return redirect('/')
        else:
            messages.error(request, 'something is wrong!')
            return render(request, 'core/add_series.html', {'form':form})
    else:
        form = seriesForm()
        return render(request, 'core/add_series.html', {'form':form})
    return render(request, 'core/add_series.html', {'form':form})


def update_series(request, slug):
    if form.instace.author != request.user:
        messages.info(request, f'{request.user} You are not authorized to update this page')
        redirect('/')
    series = articleSeries.objects.filter(slug=slug).first()
    
    if request.method == 'POST':
        form = SeriesUpdateForm(request.POST, request.FILES, instance=series)
        context = {'form':form}

        if form.is_valid():
            form.save()
            messages.success(request, "record updated successfully!")
            return redirect('/')
        for error in list(form.errors.values()):
            messages.error(request, error)
        return render(request, 'core/new-record.html', context)
    

    form = SeriesUpdateForm(instance=series)
    context = {'form':form}
    return render(request, 'core/new-record.html', context)

def delete_series(request, slug):
    matching_series = articleSeries.objects.filter(slug=slug).first()

    if request.method == "POST":
        print('>>>>>>> ',matching_series)
        try:
            matching_series.delete()
            return redirect('/')
        except Exception as e:
            messages.error(request, f'{e} >> this series still contains some articles! ')
            return redirect('/')
    else:
        return render(
            request=request,
            template_name='core/confirm_delete.html',
            context={
                "series": matching_series,
                "type": "s"
                }
            )

def create_article(request):
    
    if request.method == 'POST':
        form = articleForm(request.POST, request.FILES)
        context = { 'form':form}
        form.instance.author = request.user #to automatically fix the current user as the actual author
        
        if form.is_valid():
            form.save()
            messages.info(request, "new article created successfuly")
            return redirect('/')
            
            # return redirect('article', kwargs={f"{form.cleaned_data['series'].slug}/{form.cleaned_data.get('article_slug')}"})
            # return redirect(f"{form.cleaned_data['series'].slug}/{form.cleaned_data.get('article_slug')}")
            # return redirect('article', kwargs={'series':self.series.slug, 'article':self.article_slug})
        for error in list(form.errors.values()):
            messages.error(request, error)
        return  render(request,'core/new-record.html', context)
        
    else:
        form = articleForm()
        context = { 'form':form}
    
    return  render(request,'core/new-record.html', context)
def update_article(request, series, article_slug):
    article = Article.objects.filter(series__slug=series, article_slug=article_slug).first()
    if request.method == 'POST':
        form = ArticleUpdateForm (request.POST, request.FILES, instance=article)
        context = {'form':form}

        if form.is_valid():
            form.save()
            messages.success(request, "record updated successfully!")
            return redirect('/')
        for error in list(form.errors.values()):
            messages.error(request, error)
        return render(request, 'core/new-record.html', context)
    

    form = ArticleUpdateForm(instance=article)
    context = {'form':form}
    return render(request, 'core/new-record.html', context)


def delete_article(request,series, article):
    article = Article.objects.filter(series__slug=series, article_slug=article).first()

    if request.method == "POST":
        article.delete()
        return redirect('/')
    else:
        return render(
            request=request,
            template_name='core/confirm_delete.html',
            context={
                "series": article,
                "type": "Article"
                }
            )




