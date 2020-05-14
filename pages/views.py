
from django.shortcuts import render

from cars.models import CarsList
from carmanager.models import CarManager
from blog.models import BlogList
from .cars_info import vendor_list, models_list, engine_list, transmission_list



def index(request):
    cars = CarsList.objects.all().filter(is_published=True)[:6]
    random_car = CarsList.objects.order_by('?')[0]
    bloglist = BlogList.objects.all()
    context = {
        "vendor_list" : vendor_list,
        "models_list" : models_list,
        "engine_list" : engine_list,
        "transmission_list" : transmission_list,
        'cars' : cars,
        "request_value": request.GET,
        "rnd_car": random_car,
        "bloglist" : bloglist
        
    }
    return render(request, 'pages/index.html', context)


def about(request):
    managers = CarManager.objects.all().filter(is_published=True)[:6]
    context = {
        'managers' : managers,
        'title' : "About Us"
    }
    
    return render(request, 'pages/about.html', context)


def services(request):
    data = {"title": "Our Services"}
    return render(request, 'pages/services.html', data)


def contact(request):
    data = {"title": "Contact Us"}
    return render(request, 'pages/contacts.html', data)


def carlist(request):
   
    return render(request, 'carlist/carlist.html')

def singlecar(request):
    managers = CarManager.objects.all()
    context = {
        'managers' : managers
    }
    return render(request, 'carlist/singlecar.html', context)


def search(request):
    query = CarsList.objects.order_by("vendor")
    if "vendor" in request.GET:
        vendor = request.GET["vendor"]
        if vendor:
            query = query.filter(vendor__iexact=vendor)
            
    if "model" in request.GET:
        model = request.GET["model"]
        if model:
            query = query.filter(model__iexact=model)

    if "engine" in request.GET:
        engine = request.GET["engine"]
        if engine:
            query = query.filter(engine__iexact=engine)

    if "transmission" in request.GET:
        transmission = request.GET["transmission"]
        if transmission:
            query = query.filter(transmission__iexact=transmission)
    context = {
        "title" : "Search Car",
        "vendor_list" : vendor_list,
        "models_list" : models_list,
        "engine_list" : engine_list,
        "transmission_list" : transmission_list,
        "cars" : query,
        "request_value": request.GET
    } 
    return render(request, 'pages/search.html', context)

def blog(request):
    context = {"title": "blog"}
    return render(request, 'pages/blog.html', context)


def single_blog(request):
    context = {"title": "blog"}
    return render(request, 'blog/single_blog.html', context)