from django.shortcuts import render
from .models import Project

def proyectos(request):

    projects = Project.objects.all()

    return render(request, 'back/proyectos.html', {'projects': projects})


def proyecto(request, id):

    project = Project.objects.get(id=id)

    return render(request, 'back/proyecto.html', {'project': project})
