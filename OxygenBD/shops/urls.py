from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop_list, name='shops'),
    path('<int:pk>/', views.shop_detail, name='shop_detail'),
]