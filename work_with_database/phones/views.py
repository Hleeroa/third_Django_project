from django.http import HttpResponse
from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_type = request.GET.get('sort', 'name')
    if sort_type == 'name':
        phones = Phone.objects.order_by('name')
    elif sort_type == 'min_price':
        phones = Phone.objects.order_by('price')
    elif sort_type == 'max_price':
        phones = Phone.objects.order_by('price').reverse()
    else:
        return HttpResponse('Incorrect sort type')
    context = {
        'phones': phones,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug__contains=slug)
    context = {
        'phone': phone,
    }
    print(phone)
    return render(request, template, context)
