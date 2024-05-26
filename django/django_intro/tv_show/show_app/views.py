from django.shortcuts import render, redirect
from .models import Show
from django.contrib import messages

def index(request):
    context = {
        "shows": Show.objects.all(),
    }
    return render(request, 'index.html', context)

def delete(request, id):
    show_x = Show.objects.get(id=id)
    show_x.delete()
    return redirect('/')

def edit(request, id):
    context = {
        "show": Show.objects.get(id=id)
    }
    return render(request, 'edit_show.html', context)

def show(request, id):
    context = {
        "show": Show.objects.get(id=id)
    }
    return render(request, "view_show.html", context)

def addShow(request):
    
        return render(request,'add_show.html')
    

def editShow(request, id):
    if request.method == "POST":
        userToUpdate = Show.objects.get(id=id)
        userToUpdate.title = request.POST['title']
        userToUpdate.network = request.POST['network']
        userToUpdate.desc = request.POST['desc']
        userToUpdate.release_date = request.POST['release_date']
        userToUpdate.save()
        return redirect(f'/shows/{id}')
    context = {
        "show": Show.objects.get(id=id)
    }
    return render(request, 'edit_show.html', context)

def process (request):
    if request.method == "POST":
        current_show = Show.objects.create(
            title=request.POST['title'],
            network=request.POST['network'],
            release_date=request.POST['release_date'],
            desc=request.POST['desc']
        )
        
        return redirect (f'/shows/{current_show.id}')
        