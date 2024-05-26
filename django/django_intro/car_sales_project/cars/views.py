from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

def home(request):
    return render(request, 'cars/car_list.html')

def register(request):

    return render(request, 'registration/register.html')

def user_login(request):

    return render(request, 'registration/login.html')

def admin_login(request):
    
    return render(request, 'admin_login.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
