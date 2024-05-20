from django.urls import path
from . import views

urlpatterns = [
    path('shows/', views.index, name='index'),
    path('shows/new', views.add_show, name='add_show'),
    path('submit_show', views.submit_show, name='submit_show'),
    path('shows/<int:x>/', views.display_show, name='display_show'),  # Name for display show
    path('shows/<int:x>/edit', views.edit_show, name='edit_show'),    # Name for edit show
    path('shows/<int:x>/delete', views.destroy, name='destroy'),      # Name for destroy show
    path('submit_edit/<int:x>', views.submit_edit, name='submit_edit'),  # Name for submit edit
]
