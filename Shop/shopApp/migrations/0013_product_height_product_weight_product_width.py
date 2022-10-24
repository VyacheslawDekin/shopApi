# Generated by Django 4.1.1 on 2022-10-24 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0012_rename_stock_product_stockproduct_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='height',
            field=models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=3, default=1, max_digits=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='width',
            field=models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=15),
            preserve_default=False,
        ),
    ]
