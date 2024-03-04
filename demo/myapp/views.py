# views.py
from rest_framework import generics
from .models import Shop, Product
from .serializers import ShopSerializer, ProductSerializer
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("This is the default page.")

def home(request):
    return HttpResponse("Welcome to the home page!")

class ShopListCreate(generics.ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


