from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('sociales/', views.sociales, name='sociales'),
    path('publicaciones/', views.publicaciones, name='publicaciones'),
    path('publicacion/<int:id>', views.publicacion, name='publicacion'),
]
