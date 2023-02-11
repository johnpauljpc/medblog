from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate, logout, get_user_model
from .forms import UserRegistrationForm, loginForm, profileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import View
from django.http import HttpResponse



# Create your views here.
def userRegistration(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Accounted created successfully {user.username}')
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
                
                messages.success(request, f"Hello {user.username}! You have been logged in")
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
        user = get_user_model().objects.filter(username=username).first()
        if user:
            form = profileForm(instance = user)
            context = {'user':user, 'form':form}
            return render(request, 'profile.html', context)
        else:
            return redirect('/')
        
        
    def post( self, request, username, *args, **kwargs):
        user = request.user
        if user:
            form = profileForm( request.POST, instance = user,)
            context = {'user':user, 'form':form}

            if form.is_valid():
                form.save()
                messages.info(request, "profile is updated")

            return render(request, 'profile.html', context)
        else:
            return redirect('/')
    