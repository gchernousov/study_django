from django.http import HttpResponse
from django.shortcuts import render, reverse

from datetime import datetime
import os

def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.now()
    time_format = "%H:%M:%S"
    msg = f'Текущее время: {current_time:{time_format}}'
    return HttpResponse(msg)


def workdir_view(request):
    template_name = 'app/workdir.html'
    workdir = os.getcwd()
    files = os.listdir(path=workdir)
    context = {
        'work_dir': workdir,
        'files': files
    }
    return render(request, template_name, context)