from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from .models import Product
# Create your views here.
import random

def products(reuqest):
    all_products = Product.objects.all()

    num_products_to_display = 6

    random_products = random.sample(list(all_products), num_products_to_display)

    return random_products

def index(request):
    
    random_products=products(request)
    params = {'products': random_products}
    return render(request, 'index.html', params)
    # return HttpResponse("this is homepage")

def about(request):
    #return HttpResponse("this is about page")
    return render(request, 'about.html')

def services(request):
    #return HttpResponse("this is a service page")
    return render(request, 'services.html')



def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        description = request.POST.get('description')

        if not description:
            description = "No description provided"

        contact = Contact(name=name, email=email, description=description, date=datetime.today())
        contact.save()
        messages.success(request,"Feedback is been Submitted Succesfully")
    return render(request, 'Contact.html')

def cart(request):
    return render(request, 'cart.html')

def icecream(request):
    icecream_products = Product.objects.filter(category='Ice Cream')

    unique_subcategories = icecream_products.values_list('subcategory', flat=True).distinct()

    params = {'icecream_products': icecream_products, 'unique_subcategories': unique_subcategories}
    return render(request, 'icecream.html', params)


def cake(request):
    cake_products = Product.objects.filter(category='Cakes')

    unique_subcategories = cake_products.values_list('subcategory', flat=True).distinct()

    params = {'icecream_products': cake_products, 'unique_subcategories': unique_subcategories}
    return render(request, 'cake.html', params)


def pastries(request):
    pastry_products = Product.objects.filter(category='Pastries')

    unique_subcategories = pastry_products.values_list('subcategory', flat=True).distinct()

    params = {'icecream_products': pastry_products, 'unique_subcategories': unique_subcategories}
    return render(request, 'cake.html', params)

def waffles(request):
    waffle_products = Product.objects.filter(category='Waffles')

    unique_subcategories = waffle_products.values_list('subcategory', flat=True).distinct()

    params = {'icecream_products': waffle_products, 'unique_subcategories': unique_subcategories}
    return render(request, 'waffles.html', params)

def donuts(request):
    donut_products = Product.objects.filter(category='Donuts')

    unique_subcategories = donut_products.values_list('subcategory', flat=True).distinct()

    params = {'icecream_products': donut_products, 'unique_subcategories': unique_subcategories}
    return render(request, 'donuts.html', params)
