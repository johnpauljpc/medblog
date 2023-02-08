from django.urls import path
from .views import index, series, article

urlpatterns = [
    path('', index, name="index"),
    path('<str:series>/', series, name="series"),
    path("<str:series>/<str:article>/", article, name="article"),
    
]