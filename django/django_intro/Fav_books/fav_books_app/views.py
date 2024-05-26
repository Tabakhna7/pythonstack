from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
import bcrypt

def index(request):
    
    return render(request,"registration.html")

def creationuser(request):
    errors = User.objects.basic_validator(request.POST)
        
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        first_name=request.POST['Firstname']
        last_name=request.POST['Last_name']
        email=request.POST['mail']
        password=request.POST['Pass']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        
        user=User.objects.create(first_name=first_name, last_name=last_name,email=email , password=pw_hash)
        request.session['id']=user.id
        request.session['username']=user.first_name
        return redirect('/books')
def showBook(request):
        context={
            "users":User.objects.all(),
            "books":Book.objects.all()
        }
        return render(request,'show_book.html', context)
        
def logout(request):
    request.session.clear()
    redirect('/')
    
def login(request):
    user = User.objects.filter(email=request.POST['mail']) 
    if user: 
        logged_user = user[0] 
        if bcrypt.checkpw(request.POST['Pass'].encode(), logged_user.password.encode()):
            
            request.session['userid'] = logged_user.id
            return redirect('/books')
        
def addbook(request):

        
    titlee=request.POST['title']
    desc=request.POST['desc']
    
    Book.objects.create(title=titlee,desc=desc ,  creation=User.objects.get(id=request.session['userid']))
    
    return redirect ('/books')


