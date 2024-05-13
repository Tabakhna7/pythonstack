from django.shortcuts import render,redirect
import random
def index(request):
    
    return render(request,'index.html')
def play(request):
    request.session['random']=random.randint(10,20)
    random_num=request.session['random']
    request.session['money']+=random_num
    return redirect("/")
def play2(request):
    request.session['quest']=random.randint(-50,50)
    request.session['money']+=request.session['quest']
    return redirect('/')
def clear(request):
    del request.session['random']
    del request.session['money']
    del request.session['quest']
    
    return redirect('/')