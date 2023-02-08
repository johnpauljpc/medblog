from django.urls import path
from .views import userRegistration, loginView, logoutView

from django.contrib.auth import views as auth_view

urlpatterns = [
    path('register/', userRegistration, name='register'),
    path('login/', loginView, name="login"),
    path('logout/', logoutView, name='logout')

    ## Built in login and logout view
    # path('login/', auth_view.LoginView.as_view(template_name = 'auth/login.html'), name = "login"),
    # path('logout/', auth_view.LogoutView.as_view(template_name = 'auth/logout.html'), name = "logout"),

]