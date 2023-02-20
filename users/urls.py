from django.urls import path
from .views import (userRegistration, loginView, changePasswordView,passwordResetRequest,
                     logoutView, userProfile,activate_user, passwordResetConfirmation)

from django.contrib.auth import views as auth_view

urlpatterns = [
    path('register/', userRegistration, name='register'),
    path('login/', loginView, name="login"),
    path('logout/', logoutView, name='logout'),
    path('change-password/', changePasswordView, name='change-password'),
    path('reset-password/', passwordResetRequest, name = "reset-password"),
    path('profile/<username>/', userProfile.as_view(), name = 'profile'),
    path('activate/<uidb64>/<token>/', activate_user, name='activate'),
    path('reset/<uidb64>/<token>/', passwordResetConfirmation, name="reset-confirm"),

    ## Built in login and logout view
    # path('login/', auth_view.LoginView.as_view(template_name = 'auth/login.html'), name = "login"),
    # path('logout/', auth_view.LogoutView.as_view(template_name = 'auth/logout.html'), name = "logout"),

]