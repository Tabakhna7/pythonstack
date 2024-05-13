import random
from django.shortcuts import render,redirect

def index(request):
    if 'random' not in request.session and 'counter' not in request.session:
        request.session['random'] = random.randint(1, 100)
        request.session['counter'] = 0
    return render(request, "index.html")

def game(request):
    request.session['counter']+=1
    guessed_number=int(request.POST['random number'])
    if guessed_number > request.session['random']:
        request.session['message'] = 'Too high!'
    elif guessed_number < request.session['random']:
        request.session['message'] = 'Too low!'
    elif guessed_number == request.session['random']:
        request.session['message']='Win'
    return redirect ('/')

def destroy(request):
    del request.session['counter']
    del request.session['random']
    
    return redirect('/')