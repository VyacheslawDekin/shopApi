from rest_framework import serializers, permissions
from shopApp.models import Product, Price
from django.contrib.auth.models import User


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']


class UserCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, max_length=254)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password']


class UserPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj: User):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_superuser


class PriceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Price
        fields = ['price']


class ProductSerializer(serializers.ModelSerializer):

    # price = PriceSerializer()

    class Meta:
        model = Product
        fields = ['name', 'article', 'count', 'created', 'author']
        read_only_fields = ['created', 'author']


class ProductPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj: Product):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user or request.user.is_superuser




