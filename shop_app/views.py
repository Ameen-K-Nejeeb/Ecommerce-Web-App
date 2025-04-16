from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import ProductSerializer

# Create your views here.

@api_view({"GET"})
def products(request):
    products = products.objects.all()
    serializer = ProductSerializer(products, )