from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate, logout, get_user_model
from .forms import UserRegistrationForm, loginForm, profileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import View
from django.http import HttpResponse

from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage

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
        

def changePasswordView(request):
    pass