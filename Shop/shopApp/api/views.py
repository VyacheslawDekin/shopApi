from datetime import datetime

from rest_framework import generics, permissions
from .serializers import ProductSerializer, UsersSerializer, UserCreateSerializer, ProductPermission, UserPermission
from shopApp.models import Product, Price
from django.db.models import Q
from django.contrib.auth.models import User


class ProductListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # authentication_classes = [TokenAuthentication]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        query = Q()

        if self.request.GET.get("date"):
            date = self.request.GET.get("date")
            date = datetime.strptime(date, '%Y-%m-%d')

            # price = Price.objects.filter(created__lte=date)

            query = Q(price__created__lte=date)

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






