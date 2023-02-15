from django.urls import path
from .views import (index, series, article,
                    create_article, create_series, update_article, update_series,
                    delete_article, delete_series)

urlpatterns = [
    path('', index, name="index"),
    path('new-article/', create_article, name='new-article'),
    path('new-series/', create_series, name='new-series'),
    
    path('update/<str:series>/<str:article_slug>/', update_article, name='update-article'),
    path('delete/<series>/<article>/', delete_article, name="delete-article"),

    
    path('update/<slug>/', update_series, name='update-series'),
    path('delete/<slug>/', delete_series, name="delete-series"),
    path('<str:series>/', series, name="series"),
    path("<str:series>/<str:article>/", article, name="article"),

    
    
    
]