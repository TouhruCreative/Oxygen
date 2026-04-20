from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Review
from .forms import ReviewForm
from catalog.models import Product


@login_required
def review_create_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.product = product
            review.save()
            return redirect("catalog:product_detail", pk=product.id)
    else:
        form = ReviewForm()

    return render(request, "reviews/review_form.html", {"form": form})


@login_required
def review_update_view(request, pk):
    review = get_object_or_404(Review, pk=pk, user=request.user)

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect("catalog:product_detail", pk=review.product.id)
    else:
        form = ReviewForm(instance=review)

    return render(request, "reviews/review_form.html", {"form": form})


@login_required
def review_delete_view(request, pk):
    review = get_object_or_404(Review, pk=pk, user=request.user)

    if request.method == "POST":
        product_id = review.product.id
        review.delete()
        return redirect("catalog:product_detail", pk=product_id)

    return render(request, "reviews/review_confirm_delete.html", {"review": review})