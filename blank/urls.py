from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_link/', views.create_link, name='create_link'),
    path('password/<uuid:uuid>/', views.show_password, name='show_password'),
]