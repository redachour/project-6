from django.shortcuts import render
from .models import Mineral


def index(request):
    '''Home page view and list of all minerals'''
    minerals = Mineral.objects.all()
    return render(request, 'minerals/index.html', {'minerals': minerals})


def detail(request, pk):
    '''details view of each mineral'''
    mineral = Mineral.objects.get(pk=pk)
    return render(request, 'minerals/detail.html', {'mineral': mineral})
