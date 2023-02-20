from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate, logout, get_user_model
from .forms import (UserRegistrationForm, loginForm,
                     profileForm, changePasswordForm, passwordResetForm)
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required

from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from django.db.models import Q

from .token import account_activation_token

from django.utils.html import strip_tags


def activateEmail(request, user, to_email):
    mail_subject = 'Activate your user account.'
    message = render_to_string('template_activate_account.html', {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Dear <b>{user}</b>, please go to you email <b>{to_email}</b> inbox and click on \
            received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
    else:
        messages.error(request, f'Problem sending confirmation email to {to_email}, check if you typed it correctly.')

#### ACTIVATING ACCOUNT
def activate_user(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(request, 'Thank you for your email confirmation. Now you can login your account.')
        return redirect('login')
    else:
        messages.error(request, 'Activation link is invalid!')
    
    return redirect('/')

# Create your views here.
def userRegistration(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            activateEmail(request, user, form.cleaned_data.get('email'))
            return redirect('/')
        
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
                print(request, error)

    else:
        form = UserRegistrationForm()

    return render(request, 'auth/registration.html', {'form':form})


def loginView(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = loginForm( data = request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        if form.is_valid():
            user = authenticate(username=username , password=password
            ) 
            if user is not None:
                login(request, user)
                
                messages.success(request, f"Hello <b>{user.username}!</b> You have been logged in")
                return redirect('/')
                

        else:
            # for error in list(form.errors.values()):
            for key, error in list(form.errors.items()):
                if key == 'captcha' and error[0] == 'This field is required.':
                    messages.error(request, 'You must pass the reCAPTCHA test before proceeding')
                    continue
                messages.error(request, error) 
                print(error)

    form = loginForm() 
    
    return render(request, "auth/login.html", {'form': form})

def logoutView(request):
    
    logout(request)
    messages.info(request, "You have been logged out")
    return render(request, 'auth/logout.html')

class userProfile(View):
    def get( self, request, username, *args, **kwargs):
        try:
            user = get_user_model().objects.get(username=username)
            form = profileForm(instance = user)
            form.fields['description'].widget.attrs = {'rows': 2}
            
            context = {'form':form}
            return render(request, 'profile.html', context)
        except:
            return redirect('/')
        
        
    def post( self, request, username, *args, **kwargs):
        user = request.user
        if user:
            form = profileForm( request.POST, request.FILES, instance = user)
            context = {'user':user, 'form':form}

            if form.is_valid():
                user_form = form.save()
                messages.info(request, f"{user_form.username}, Your profile has been updated")

            return render(request, 'profile.html', context)
        else:
            return redirect('/')
        
@login_required(login_url='login')
def changePasswordView(request):
    user = request.user
    print(user)
    form = changePasswordForm(user)
    context = {
        'form':form
    }

    if request.method == 'POST':
        form = changePasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'password changed successfully, kindly login with new password')
            return redirect('login')
        for error in list(form.errors.values()):
            messages.error(request, error)
    return render(request, 'auth/change-password.html', context)


def passwordResetRequest(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = passwordResetForm(data=request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            associated_user = get_user_model().objects.filter(Q(email=user_email)).first()
            if associated_user:
                subject = "Password Reset request"
                message = render_to_string("template_reset_password.html", {
                    'user': associated_user,
                    'domain': get_current_site(request).domain,
                    'uid': urlsafe_base64_encode(force_bytes(associated_user.pk)),
                    'token': account_activation_token.make_token(associated_user),
                    "protocol": 'https' if request.is_secure() else 'http'
                })
                email = EmailMessage(subject, message, to=[associated_user.email])
                if email.send():
                    messages.success(request,
                        """
                        <h2>Password reset sent</h2><hr>
                        <p>
                            We've emailed you instructions for setting your password, if an account exists with the email you entered. 
                            You should receive them shortly.<br>If you don't receive an email, please make sure you've entered the address 
                            you registered with, and check your spam folder.
                        </p>
                        """
                    )
                else:
                    messages.error(request, "Problem sending reset password email, <b>SERVER PROBLEM</b>")

            return redirect('/')
        

        for key, error in list(form.errors.items()):
            messages.error(request,  error)
            if key == 'captcha' and error[0] == 'This field is required.':
                messages.error(request, "You must pass the reCAPTCHA test")
                
        
                



    form = passwordResetForm()
    context = {
        'form':form
    }
    return render(request, 'auth/password-reset.html', context)

def passwordResetConfirmation(request, uidb64, token):

    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        if request.method == 'POST':
            form = changePasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Your password has been set. You may go ahead and <b>log in </b> now.")
                return redirect('/')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)

        form = changePasswordForm(user)
        context = {
            'form':form
        }
        return render(request, 'auth/change-password.html', context)
    else:
        messages.error(request, "Link is expired")

    messages.error(request, 'Something went wrong, redirecting back to Homepage')
    return redirect("/")


    
