from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from API_Side.models import Store, Product, Category, Customer, Account, Order
from API_Side.serializers import StoreSerializer, AccountSerializer, ProductSerializer, CategorySerializer, CustomerSerializer, OrderSerializer

# Create your views here.


class StoreView(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]


class StoreViewSet(viewsets.ModelViewSet):
    serializer_class = StoreSerializer
    queryset = Store.objects.all()
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    

class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

