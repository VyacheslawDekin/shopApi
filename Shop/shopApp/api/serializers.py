from datetime import datetime

from django.db.models import Q
from rest_framework import serializers, permissions, status
from rest_framework.response import Response

from shopApp.models import Product, Price, StockProduct
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
        fields = ['product', 'price']


class ProductSerializer(serializers.ModelSerializer):

    # price = PriceSerializer()
    class Meta:
        model = Product
        fields = ['name', 'article', 'description', 'width', 'height', 'weight', 'created', 'author']
        read_only_fields = ['created', 'author']


class ProductPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj: Product):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user or request.user.is_superuser


class ProductDetailsViewSerializer(serializers.ModelSerializer):

    stock_product = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['name', 'article', 'description', 'width', 'height', 'weight', 'created', 'author', 'stock_product']
        read_only_fields = ['created', 'author', 'width', 'height', 'weight', 'stock_product']

    def to_representation(self, instance: Product):
        ret = super().to_representation(instance)
        try:
            query = Q(product=instance)

            date = self.context.get('request').query_params.get('date')
            if date:
                try:
                    date = datetime.strptime(date, '%Y-%m-%d')
                    query &= Q(created__lte=date)
                except Exception:
                    return Response(data='invalid date format', status=status.HTTP_400_BAD_REQUEST)

            price_queryset = Price.objects.filter(query).order_by('-created').first()
            price = price_queryset.price
        except:
            price = 0

        ret['price'] = price
        return ret


class StockProductSerializer(serializers.ModelSerializer):

    product = serializers.CharField(source='product.name')

    class Meta:
        model = StockProduct
        fields = ['stock', 'product', 'count']

#
# class StockProductSerializerCreate(serializers.ModelSerializer):
#
#     class Meta:
#         model = StockProduct
#         fields = ['stock', 'product', 'count']



