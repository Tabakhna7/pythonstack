from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
     context = {
          'Movies' : Movie.objects.all(),
          'Actors': Actor.objects.all()
     }     
     return render (request,'index.html',context)
