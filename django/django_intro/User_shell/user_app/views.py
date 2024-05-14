from django.shortcuts import render, redirect
from .models import User

def index(request):
    Data = { "Users":User.objects.all()}
    return render(request, "index.html", Data)

def add(request):
   
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['Email']
        age = request.POST['Age']
        User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            age=age
        )  
        
        return redirect('/')

