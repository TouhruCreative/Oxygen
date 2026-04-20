from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Product, Category
from .forms import ProductForm, CategoryForm

from users.permissions import role_required

def product_list_view(request):
    products = Product.objects.all()
    return render(request, "catalog/product_list.html", {"products": products})


def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "catalog/product_detail.html", {"product": product})


@login_required
def product_create_view(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("catalog:product_list")
    else:
        form = ProductForm()

    return render(request, "catalog/product_form.html", {"form": form})


@login_required
def product_update_view(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("catalog:product_detail", pk=product.pk)
    else:
        form = ProductForm(instance=product)

    return render(request, "catalog/product_form.html", {"form": form})


@login_required
def product_delete_view(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        product.delete()
        return redirect("catalog:product_list")

    return render(request, "catalog/product_confirm_delete.html", {"product": product})


def category_list_view(request):
    categories = Category.objects.all()
    return render(request, "catalog/category_list.html", {"categories": categories})

@role_required(["admin", "moderator"])
def category_create_view(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("catalog:category_list")
    else:
        form = CategoryForm()

    return render(request, "catalog/category_form.html", {"form": form})

@role_required(["admin", "moderator"])
def category_update_view(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect("catalog:category_list")
    else:
        form = CategoryForm(instance=category)

    return render(request, "catalog/category_form.html", {"form": form})

@role_required(["admin", "moderator"])
def category_delete_view(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == "POST":
        category.delete()
        return redirect("catalog:category_list")

    return render(request, "catalog/category_confirm_delete.html", {"category": category})