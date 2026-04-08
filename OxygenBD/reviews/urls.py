from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:product_id>/', views.review_create, name='review_create'),
]