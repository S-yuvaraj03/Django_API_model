# urls.py
from django.urls import path
from .views import ShopListCreate, ProductListCreate
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('shops/', ShopListCreate.as_view(), name='shop-list-create'),
    path('products/', ProductListCreate.as_view(), name='product-list-create'),
]
