from django.shortcuts import render, redirect

from django.contrib.auth import login, get_user_model
from .forms import UserRegistrationForm
# Create your views here.
def userRegistration(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        
        else:
            for error in list(form.errors.values()):
                print(request, error)

    else:
        form = UserRegistrationForm()

    return render(request, 'core/auth/registration.html', {'form':form})
