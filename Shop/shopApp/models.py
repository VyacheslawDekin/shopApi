from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=200, null=False)
    article = models.CharField(max_length=11, null=False)
    count = models.DecimalField(max_digits=15, decimal_places=3, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.article + ' | ' + self.name


class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=15, decimal_places=2, null=False)
    created = models.DateTimeField(auto_now_add=True)










