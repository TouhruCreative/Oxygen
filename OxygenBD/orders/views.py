from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from catalog.models import ProductVariant
from rest_framework.permissions import IsAuthenticated
from users.api.permissions import IsAdminOrModerator

@login_required
def orders_list_view(request):
    if request.user.role in ["admin", "moderator"]:
        orders = Order.objects.all()
    else:
        orders = request.user.order_set.all()

    return render(request, "orders/orders_list.html", {
        "orders": orders
    })


@login_required
def order_detail_view(request, pk):
    order = get_object_or_404(Order, pk=pk, user=request.user)

    return render(request, "orders/order_detail.html", {
        "order": order,
        "items": order.items.all()
    })


@login_required
def create_order_view(request):
    if request.method == "POST":
        order = Order.objects.create(user=request.user)

        # ТЕСТОВЫЙ вариант (потом заменим на cart)
        product = ProductVariant.objects.first()

        if product:
            OrderItem.objects.create(
                order=order,
                product_variant=product,
                quantity=1,
                price=product.price
            )

            order.total_price = product.price
            order.save()

        return redirect("order_detail", pk=order.id)

    return render(request, "orders/create_order.html")