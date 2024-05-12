from django.shortcuts import render,redirect
def index(request):
    if 'counter' and 'visit' not in request.session:
        request.session['counter']=0
        request.session['visit']=0
    
    else:
        request.session['counter']+=1
    
    return render (request, "index.html")


def destroy(request):
    
    del request.session['visit']
    del request.session['counter']
    
    return redirect('/')

def addTwo(request):

    request.session['visit']+=2
    request.session['counter']=-1
    return  redirect('/')   
        
    
def incr(request):
    request.session['visit']=int(request.POST['user-input'])
    request.session['counter']=-1
    return redirect('/')