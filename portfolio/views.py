from django.shortcuts import render
from .models import Project


def home(request):
    projects = Project.objects.all().order_by('id').reverse()
    return render(request, 'portfolio/home.html', {'projects': projects})
