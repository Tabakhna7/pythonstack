from django.shortcuts import render, redirect, get_object_or_404
from .models import Show

def index(request):
    data = {
        "shows": Show.objects.all()
    }
    return render(request, "index.html", data)

def add_show(request):
    return render(request, "add_shows.html")

def submit_show(request):
    Show.objects.create(
        title=request.POST['title'],
        network=request.POST['network'],
        release_date=request.POST['release_date'],
        desc=request.POST['desc']
    )
    return redirect("/shows/")

def display_show(request, x):
    show = get_object_or_404(Show, id=x)
    return render(request, "tv_shows.html", {'show': show})

def edit_show(request, x):
    show = get_object_or_404(Show, id=x)
    return render(request, "edit.html", {'show': show})

def submit_edit(request, x):
    show = get_object_or_404(Show, id=x)
    show.title = request.POST['title']
    show.network = request.POST['network']
    show.release_date = request.POST['release_date']
    show.desc = request.POST['description']
    show.save()
    return redirect("/shows/")
    
def destroy(request, x):
    show = get_object_or_404(Show, id=x)
    show.delete()
    return redirect('/shows/')
