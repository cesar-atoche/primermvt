from django.urls import path
from familia import views

urlpatterns = [
    path('', views.inicio),  
    # path('borra/', views.borrar),  
]