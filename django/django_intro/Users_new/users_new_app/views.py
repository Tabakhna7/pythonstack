from django.shortcuts import render,redirect
from .models import User
def index(request):
    data={
        'usrs':User.objects.all()
    }
    return render(request,"index.html",data)
def addUser(request):
    if request.method=='POST':
        
        User.objects.create(first_name=request.POST['frst_name'],
                            last_name=request.POST['lst_name'],
                            email=request.POST['mail'],
                            age=request.POST['AGE'])
    return redirect('/')