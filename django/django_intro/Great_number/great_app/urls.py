from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('number', views.game),
    path('clear',views.destroy),
]