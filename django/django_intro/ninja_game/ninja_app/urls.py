from django.urls import path
from . import views	# the . indicates that the views file can be found in the same directory as this file
                    
urlpatterns = [
    path('', views.index),
    path('process_money', views.play),
    path('process_money2', views.play2),
    path('clear' ,views.clear),
]