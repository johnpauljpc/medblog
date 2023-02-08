from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate, logout, get_user_model
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

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
        form = AuthenticationForm( data = request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        if form.is_valid():
            user = authenticate(username=username, password=password
            )
            if user is not None:
                login(request, user)
                
                messages.success(request, f"Hello {user.username}! You have been logged in")
                return redirect('/')
                

        else:
            for error in list(form.errors.values()):
                messages.error(request, error) 

    form = AuthenticationForm() 
    
    return render(request, "auth/login.html", {'form': form})

def logoutView(request):
    logout(request)
    messages.info(request, "You have been logged out")
    return render(request, 'auth/logout.html')