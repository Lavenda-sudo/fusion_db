from django.shortcuts import render, redirect, get_object_or_404
from.models import Products
from.forms import ProductForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout

@login_required
def home(request):
    products= Products.objects.all() #select * from products
    return render(request, "home.html",{"products": products})

@login_required
def add(request):
        if request.method == "POST":
            form = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                product = form.save()
                messages.success(request, f"{product.name} successfully added")
                return redirect('home')
        else:
            form = ProductForm()
        return render(request, "add.html", {"form": form})
    # Products.objects.create(name="Unga",
    #                        code="0136677",
    #                        price=518.0,
    #                        cost=488.0,
    #                        category="Foods",
    #                        for_sale=True
    #                        )

@login_required
def delete_products(request, id):
    products = Products.objects.get(id=id)
    products.delete()
    messages.warning(request, f"{products.name} deleted permanently")
    return redirect('home')


@login_required
def edit_products(request, id):
    products = Products.objects.get(id=id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=products)
        if form.is_valid():
            form.save()
            messages.success(request, f"{products.name} successfully updated")
            return redirect('home')
    else:
        form = ProductForm(instance=products)
    return render(request, "edit.html",{"form":form}) # or whatever you have

@login_required
def details(request, id):
    product = get_object_or_404(Products, id=id)
    return render(request, "details.html", {"product": product})  # or whatever you have

def signin(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            messages.success(request, f"successfully logged in")
            return redirect('home')
        else:
            form = AuthenticationForm()
        return render(request, "registration/login.html", {"form": form})

def signup(request):
    return None

@login_required
def signout(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')

# group(perms)


