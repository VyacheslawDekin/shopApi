from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Product, Price


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ['article', 'name', 'count', 'author', 'created', 'price']
    search_fields = ['article', 'author']

    ordering = ['name']
    list_filter = ['article', 'count']

    fieldsets = (
        ('Заголовок, содержимое', {'fields': ['article', 'name', 'count']}),
        ('Автор, дата создания', {'fields': ['author', 'created']}),
    )

    readonly_fields = ['created']

    @admin.display(description='price')
    def price(self, product: Product):
        price_dict = Price.objects.filter(product=product).order_by('-created').values('price').first()
        price = price_dict.get('price') if price_dict else 0

        return mark_safe(f"""
            <div style="color: green;" > {price} </div>   
            """)


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):

    list_display = ['product', 'price']
    search_fields = ['product', 'price']

    ordering = ['product']
    list_filter = ['product', 'price']

    fieldsets = (
        ('Продукт, значение', {'fields': ['product', 'price']}),
        ('Дата создания', {'fields': ['created']}),
    )

    readonly_fields = ['created']

