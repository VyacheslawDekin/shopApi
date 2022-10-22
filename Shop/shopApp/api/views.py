from datetime import datetime

from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.views import Response, status

from .serializers import ProductSerializer, UsersSerializer, UserCreateSerializer, ProductPermission, UserPermission, ProductDetailsViewSerializer, StockProductSerializer
from shopApp.models import Product, Price, StockProduct
from django.db.models import Q
from django.contrib.auth.models import User


class ProductListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ProductDetailsViewSerializer
    queryset = Product.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # authentication_classes = [TokenAuthentication]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        query = Q()

        if self.request.GET.get("article"):
            article = self.request.GET.get("article")
            query &= Q(article=article)

        products = Product.objects.filter(query)

        return products


class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [ProductPermission]

    lookup_field = 'article'
    lookup_url_kwarg = 'article'

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ProductDetailsViewSerializer

        return ProductSerializer


class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return UsersSerializer

        return UserCreateSerializer


class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [UserPermission]

    lookup_field = 'username'
    lookup_url_kwarg = 'username'


class StockProductListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = StockProductSerializer
    queryset = StockProduct.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        article = self.request.POST.get('product')
        product = get_object_or_404(Product, article=article)

        serializer.save(product=product)

class StockProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StockProductSerializer
    queryset = StockProduct.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]













