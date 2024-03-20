from django.shortcuts import render, HttpResponse
from datetime import datetime, timedelta
from home.models import Contact
from django.contrib import messages
from .models import Product
import random

# Define a global variable to store the last refresh time
last_refresh_time = None

def should_refresh_products():
    global last_refresh_time

    if last_refresh_time is None:
        # If last_refresh_time is not set, set it to the current time
        last_refresh_time = datetime.now()
        return True

    # Calculate the time difference between now and last_refresh_time
    time_difference = datetime.now() - last_refresh_time

    # Check if a day has passed (86400 seconds in a day)
    if time_difference.total_seconds() >= 86400:
        # If a day has passed, update last_refresh_time and return True to refresh products
        last_refresh_time = datetime.now()
        return True

    return False

def get_random_products():
    all_products = Product.objects.all()

    num_products_to_display = 6

    random_products = random.sample(list(all_products), num_products_to_display)

    return random_products

def products(request):
    if should_refresh_products():
        random_products = get_random_products()
    else:
        # Return previously generated random products without refreshing
        random_products = None

    return random_products

def index(request):
    random_products = products(request)

    if random_products is None:
        # If random_products is None, it means products were not refreshed, so get them again
        random_products = get_random_products()

    params = {'products': random_products}
    return render(request, 'index.html', params)

def about(request):
    return render(request, 'about.html')

def services(request):
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
        messages.success(request, "Feedback has been submitted successfully")

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

    params = {'cake_products': cake_products, 'unique_subcategories': unique_subcategories}
    return render(request, 'cake.html', params)

def pastries(request):
    pastry_products = Product.objects.filter(category='Pastries')

    unique_subcategories = pastry_products.values_list('subcategory', flat=True).distinct()

    params = {'pastry_products': pastry_products, 'unique_subcategories': unique_subcategories}
    return render(request, 'pastries.html', params)

def waffles(request):
    waffle_products = Product.objects.filter(category='Waffles')

    unique_subcategories = waffle_products.values_list('subcategory', flat=True).distinct()

    params = {'waffle_products': waffle_products, 'unique_subcategories': unique_subcategories}
    return render(request, 'waffles.html', params)

def donuts(request):
    donut_products = Product.objects.filter(category='Donuts')

    unique_subcategories = donut_products.values_list('subcategory', flat=True).distinct()

    params = {'donut_products': donut_products, 'unique_subcategories': unique_subcategories}
    return render(request, 'donuts.html', params)
