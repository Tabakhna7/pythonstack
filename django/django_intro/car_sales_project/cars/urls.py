from django.urls import path
from cars import views

urlpatterns = [
    # Other URL patterns
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('admin-login/', views.admin_login, name='admin_login'),
]
