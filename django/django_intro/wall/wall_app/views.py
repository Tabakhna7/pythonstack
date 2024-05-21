from django.shortcuts import render

from django.shortcuts import render, render,redirect
from django.contrib import messages
from .models import User, Message , Comment
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
        'usr':User.objects.get(id=request.session['userid']),
        'msgs':Message.objects.all(),
        'comments':Comment.objects.all()
            }
    return render(request,'wall.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')

def msg(request,id):
    user_new=User.objects.get(id=id)
    Message.objects.create(users=user_new , message=request.POST['message_posted'] )
    return redirect('/success')
    