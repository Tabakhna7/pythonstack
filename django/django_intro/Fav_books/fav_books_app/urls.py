from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('creating_user',views.creationuser),
    path('books',views.showBook),
    path('logout',views.logout),
    path('login',views.login),
    path('addbook',views.addbook)

    
    ,
]
