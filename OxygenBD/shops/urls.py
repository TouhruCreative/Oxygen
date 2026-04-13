from django.urls import path
from .views import (
    shop_list_view,
    shop_detail_view,
    shop_create_view,
    shop_update_view,
    shop_delete_view
)

urlpatterns = [
    path("", shop_list_view, name="shop_list"),
    path("<int:pk>/", shop_detail_view, name="shop_detail"),
    path("create/", shop_create_view, name="shop_create"),
    path("<int:pk>/edit/", shop_update_view, name="shop_edit"),
    path("<int:pk>/delete/", shop_delete_view, name="shop_delete"),
]