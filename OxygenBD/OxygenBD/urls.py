from django.contrib import admin
from django.urls import path, include
from catalog.views import product_list_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', product_list_view),
    path('', include('users.urls')),
    path('shops/', include('shops.urls')),
    path('catalog/', include('catalog.urls')),
    #path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
    path('reviews/', include('reviews.urls')),
]