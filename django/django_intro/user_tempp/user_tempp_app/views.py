from django.shortcuts import render,redirect
from .models import User
def index(request):
    Data={"Usrs":User.objects.all() }
    return render(request , "index.html", Data)
def addUser(request):
    if request.method=="POST":
        frst_name=request.POST['First_name']
        lst_name=request.POST['Last_name']
        eemail=request.POST['mail']
        userAge=request.POST['Age']
        User.objects.create(first_name=frst_name, last_name=lst_name,email=eemail , age=userAge)
        return redirect('/')    