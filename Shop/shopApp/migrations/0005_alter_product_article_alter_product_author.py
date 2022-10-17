# Generated by Django 4.1.1 on 2022-09-30 20:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shopApp', '0004_product_author_product_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='article',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='product',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
