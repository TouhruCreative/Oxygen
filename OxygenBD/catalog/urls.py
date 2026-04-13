from django.urls import path
from .views import *

app_name = "catalog"

urlpatterns = [
    path("", product_list_view, name="product_list"),
    path("<int:pk>/", product_detail_view, name="product_detail"),
    path("create/", product_create_view, name="product_create"),
    path("<int:pk>/edit/", product_update_view, name="product_update"),
    path("<int:pk>/delete/", product_delete_view, name="product_delete"),

    path("categories/", category_list_view, name="category_list"),
    path("categories/create/", category_create_view, name="category_create"),
    path("categories/<int:pk>/edit/", category_update_view, name="category_update"),
    path("categories/<int:pk>/delete/", category_delete_view, name="category_delete"),
]