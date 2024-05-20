from django.shortcuts import render, render,redirect
from django.contrib import messages
from .models import User
import bcrypt 

def index(request):
    Data= {'usr': User.objects.all()}
    return render(request,'index.html', Data)


def add(request):
    if request.method == 'POST':
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value,extra_tags="invalid")
            return redirect('/')
        
        else:
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()     
            user_n= User.objects.create(first_name=request.POST['first_name'],
                                        last_name=request.POST['last_name'],
                                        email=request.POST['email'], 
                                        password=pw_hash)
            request.session['userid']=user_n.id
                
        return redirect('/success')
    
    
def login(request):

    email = User.objects.filter(email=request.POST['login_email'])
    if email: 
        logged_email = email[0] 
        if bcrypt.checkpw(request.POST['login_password'].encode(), logged_email.password.encode()):
            request.session['userid'] = logged_email.id
            return redirect('/success')
    messages.error(request,"Email or Password is invalid!", extra_tags = "wrong")    
    return redirect("/")

def success(request):
    if "userid" not in request.session:
        return redirect('/')

    context={
        'usr':User.objects.get(id=request.session['userid'])
            }
    return render(request,'success.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')