from django.shortcuts import render, redirect
from.models import Products
from.forms import ProductForm

def home(request):
    products= Products.objects.all() #select * from products
    return render(request, "home.html",{"products": products})

def add(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProductForm()
    return render(request, "add.html",{"form":form}) # or whatever you have
    # Products.objects.create(name="Unga",
    #                        code="0136677",
    #                        price=518.0,
    #                        cost=488.0,
    #                        category="Foods",
    #                        for_sale=True
    #                        )