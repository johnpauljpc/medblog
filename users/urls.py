from django.urls import path
from .views import userRegistration

urlpatterns = [
    path('register/', userRegistration, name='register')

]