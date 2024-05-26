from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),	
    path('addBook',views.addBook),
    path('books/<int:x>',views.showBook),
    path('authors',views.authors_index),
    path('add_author',views.addAuthor),
    path('authors/<int:y>',views.view_authors),
]
