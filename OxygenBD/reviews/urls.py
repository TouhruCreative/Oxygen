from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
    path("create/<int:product_id>/", views.review_create_view, name="review_create"),
    path("<int:pk>/edit/", views.review_update_view, name="review_update"),
    path("<int:pk>/delete/", views.review_delete_view, name="review_delete"),
]