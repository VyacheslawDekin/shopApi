from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Product, Price, StockProduct, Stock

admin.site.register(Stock)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ['article', 'name', 'author', 'created', 'price_']
    search_fields = ['article', 'author']

    ordering = ['name']
    list_filter = ['article']

    fieldsets = (
        ('article, name, description', {'fields': ['article', 'name', 'description']}),
        ('width, height, weight', {'fields': ['width', 'height', 'weight']}),
        ('author, created', {'fields': ['author', 'created']}),
    )

    readonly_fields = ['created']

    @admin.display(description='price')
    def price_(self, product: Product):
        price_dict = Price.objects.filter(product=product).order_by('-created').values('price').first()
        price = price_dict.get('price') if price_dict else 0

        return mark_safe(f"""
            <div style="color: green;" > {price} </div>   
            """)


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):

    list_display = ['product', 'price', 'created']
    search_fields = ['product', 'price']

    ordering = ['product']
    list_filter = ['product', 'price']

    fieldsets = (
        ('Product, price', {'fields': ['product', 'price']}),
        ('Created', {'fields': ['created']}),
    )

    readonly_fields = ['created']


@admin.register(StockProduct)
class StockProductAdmin(admin.ModelAdmin):

    list_display = ['product', 'stock', 'count']
    search_fields = ['product', 'stock', 'count']

    ordering = ['product', 'stock', 'count']
    list_filter = ['product', 'stock', 'count']

    fieldsets = (
        ('product, stock, count', {'fields': ['stock', 'product', 'count']}),
    )

