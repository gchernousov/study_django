from django.shortcuts import render, redirect

from .models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort_response = request.GET.get('sort')
    if sort_response == 'min_price':
        phones = Phone.objects.order_by('price')
    elif sort_response == 'max_price':
        phones = Phone.objects.order_by('-price')
    elif sort_response == 'name':
        phones = Phone.objects.order_by('name')
    else:
        phones = Phone.objects.all()
    template = 'catalog.html'
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
