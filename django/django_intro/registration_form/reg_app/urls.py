from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('process', views.add),	
    path('process2', views.login),
    path('success', views.success),
    path('logout', views.logout),
]
