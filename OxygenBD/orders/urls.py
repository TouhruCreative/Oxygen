from django.urls import path
from .views import orders_list_view, order_detail_view, create_order_view

urlpatterns = [
    path("", orders_list_view, name="orders_list"),
    path("<int:pk>/", order_detail_view, name="order_detail"),
    path("create/", create_order_view, name="create_order"),
]