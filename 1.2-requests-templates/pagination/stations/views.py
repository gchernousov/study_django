from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator

import csv
from pagination.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    csv_file = open(BUS_STATION_CSV, newline='', encoding='utf-8')
    bus_stations_data = list(csv.DictReader(csv_file))

    page_parameter = int(request.GET.get('page', 1))
    paginator = Paginator(bus_stations_data, 10)
    page = paginator.get_page(page_parameter)
    current_bus_stations = page.object_list

    context = {
        'bus_stations': current_bus_stations,
        'page': page,
    }
    csv_file.close()
    return render(request, 'stations/index.html', context)
