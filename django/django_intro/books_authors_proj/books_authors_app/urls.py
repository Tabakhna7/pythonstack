from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add', views.add_book),
    path('books/<int:x>', views.view_book),
    path('authors', views.authors_index),
    path('authors/add', views.add_author),
    path('authors/<int:id>', views.view_author),
]