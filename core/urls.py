from django.urls import path
from .views import index, series

urlpatterns = [
    path('', index, name="index"),
    path('<str:series>/', series, name="series"),

]