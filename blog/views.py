from django.shortcuts import render
from .models import Post

def inicio(request):

    return render(request, 'blog/inicio.html', {})


def sociales(request):

    return render(request, 'blog/sociales.html', {})


def publicaciones(request):

    publicaciones = Post.objects.all()

    return render(request, 'blog/publicaciones.html', {'publicaciones': publicaciones})


def publicacion(request, id):

    publicacion = Post.objects.get(id=id)

    return render(request, 'blog/publicacion.html', {'publicacion': publicacion})

