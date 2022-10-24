from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=200, null=False)
    article = models.CharField(max_length=11, null=False)
    description = models.CharField(max_length=500, blank=True, default="")
    width = models.DecimalField(max_digits=15, decimal_places=3, blank=True, default=0)
    height = models.DecimalField(max_digits=15, decimal_places=3, blank=True, default=0)
    weight = models.DecimalField(max_digits=15, decimal_places=3, blank=True, default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.article} | {self.name}'


class Price(models.Model):
    product = models.ForeignKey(Product, related_name='price', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=15, decimal_places=2, null=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.price}'


class Stock(models.Model):
    name = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.name


class StockProduct(models.Model):
    product = models.ForeignKey(Product, related_name='stock_product', on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    count = models.DecimalField(max_digits=15, decimal_places=3, null=False)

    class Meta:
        verbose_name = 'Product in stock'
        verbose_name_plural = 'Products in stock'

        unique_together = ('product', 'stock')

    def __str__(self):
        return f'stock: {self.stock}, count: {self.count}'











