from django.urls import path     
from . import views
urlpatterns = [
    path('shows/new',views.addShow),
    path('shows/processv',views.process),
    path('', views.index ),
    path('update/<int:id>',views.editShow),
    path('shows/<int:id>',views.show),
    path("<int:id>/destroy", views.delete),
    path('<int:id>/edit',views.edit),
    
]


