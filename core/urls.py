from django.urls import path
from .views import (index, series, article,create_article, create_series, update_article, update_series,
                    delete_article, delete_series, subscribe, newsletter)
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', index, name="index"),
    path('new-article/', create_article, name='new-article'),
    path('new-series/', create_series, name='new-series'),
    path('subscribe/', subscribe, name='subscribe'),
    path('newsletter/', newsletter, name="newsletter"),
    
    path('update/<str:series>/<str:article_slug>/', update_article, name='update-article'),
    path('delete/<series>/<article>/', delete_article, name="delete-article"),

    
    path('update/<slug>/', update_series, name='update-series'),
    path('delete/<slug>/', delete_series, name="delete-series"),
    path('<str:series>/', series, name="series"),
    path("<str:series>/<str:article>/", article, name="article"),
    # path('<series>/<article>/upload_image', csrf_exempt(upload_image), name="upload_image"),

    
    
    
]