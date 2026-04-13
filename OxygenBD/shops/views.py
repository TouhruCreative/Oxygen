from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Shop

def shop_list_view(request):
    shops = Shop.objects.all()

    return render(request, "shops/shop_list.html", {
        "shops": shops
    })

def shop_detail_view(request, pk):
    shop = get_object_or_404(Shop, id=pk)

    return render(request, "shops/shop_detail.html", {
        "shop": shop
    })

@login_required
def shop_create_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")

        Shop.objects.create(
            owner=request.user,
            name=name,
            description=description,
            rating=0  # по умолчанию
        )

        return redirect("shop_list")

    return render(request, "shops/shop_create.html")

@login_required
def shop_update_view(request, pk):
    shop = get_object_or_404(Shop, id=pk)

    # защита: только владелец
    if shop.owner != request.user:
        return redirect("shop_list")

    if request.method == "POST":
        shop.name = request.POST.get("name")
        shop.description = request.POST.get("description")
        shop.save()

        return redirect("shop_detail", pk=shop.id)

    return render(request, "shops/shop_edit.html", {
        "shop": shop
    })

@login_required
def shop_delete_view(request, pk):
    shop = get_object_or_404(Shop, id=pk)

    if shop.owner != request.user:
        return redirect("shop_list")

    if request.method == "POST":
        shop.delete()
        return redirect("shop_list")

    return render(request, "shops/shop_delete.html", {
        "shop": shop
    })

