from django.shortcuts import render
from .models import Place


def display(request):
    obj = Place.objects.all()
    return render(request, 'index.html', {'display': obj})