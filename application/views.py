from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.conf import settings
from django.http import HttpResponse
from .models import *
from .forms import *


def index1(request):
    return render(request, 'application/index1.html', {'title': 'Web site page'})

def index2(request):
    games = Games.objects.all()

    return render(request, 'application/index2.html', {'games': games})

def index3(request):
    error = ''
    if request.method == 'POST':
        form = GamesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('application/index2.html')
        else:
            error = 'Form filled out incorrect'

    context = {
        'form': form,
        'error': error
    }
    return render(request, 'application/index3.html', context=context)

def index4(request):
    return render(request, 'application/index4.html')

def index5(request):
    return render(request, 'application/index5.html')

