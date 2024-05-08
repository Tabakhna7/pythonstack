from django.shortcuts import render, HttpResponse ,redirect
from django.http import JsonResponse

def root (request):
    
    return redirect ('/blogs')

def index(request):
    return HttpResponse ('placeholder to later display a list of all blogs')


def new(request):
    
    return HttpResponse('placeholder to display a new form to create a new blog')

def create (request):
    return redirect('/')

def shaw(request,number):
    return HttpResponse(f'placeholder to display blog number: {number} ')

def edit (request,number):
    return HttpResponse(f'placeholder to edit blog {number}')

def destroy(request , number):
    return redirect ('/blogs')

def json(request):
    var= {
        "title": "My first blog",
        "content": "lorem, ipusm sa sda wq eqw eqw eqw es ad as",
    }
    return JsonResponse(var)