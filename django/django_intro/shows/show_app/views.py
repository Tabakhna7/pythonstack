from django.shortcuts import render, redirect
from .models import Show
from django.contrib import messages

def red(request):
    return redirect('/shows/')

def index(request):
    context = {
        "shows": Show.objects.all(),
    }
    return render(request, "index.html", context)

def new(request):
    return render(request, "add_shows.html")

def add(request):
    if request.method == "POST":
        title = request.POST.get('title', '')
        network = request.POST.get('network', '')
        release_date = request.POST.get('release_date', '')
        desc = request.POST.get('desc', '')

        errors = Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('shows/new')
        else:
            obj_x = Show.objects.create(title=title, network=network, release_date=release_date, desc=desc)
            messages.success(request, "Show successfully added")
            return redirect(f"shows/{obj_x.id}")
    return redirect('/shows/new')

def delete(request, id):
    show = Show.objects.get(id=id)
    show.delete()
    return redirect('/shows/')

def show(request, id):
    data = {
        "show": Show.objects.get(id=id)
    }
    return render(request, "show.html", data)

def edit(request, id):
    data = {
        "show": Show.objects.get(id=id)
    }
    return render(request, 'edit.html', data)

def update(request, id):
    if request.method == "POST":
        title = request.POST.get('title', '')
        network = request.POST.get('network', '')
        release_date = request.POST.get('release_date', '')
        desc = request.POST.get('desc', '')

        errors = Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/shows/{id}/edit')
        else:
            edit_show = Show.objects.get(id=id)
            edit_show.title = title
            edit_show.network = network
            edit_show.desc = desc
            edit_show.release_date = release_date
            edit_show.save()
            messages.success(request, "Show successfully updated")
            return redirect('/')
    return redirect(f'/shows/{id}/edit')
