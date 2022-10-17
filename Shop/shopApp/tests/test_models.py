import django
django.setup()
from django.test import TestCase
from shopApp import models
from django.contrib.auth.models import User


class ProductTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User(username='test_user')
        user.set_password('password')
        user.save()

        models.Product.objects.create(
            name='Name',
            article='09235',
            count=34,
            author=user
        )

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_model_product_create(self):
        product = models.Product.objects.get(article='09235')
        max_length_name = product._meta.get_field('name').max_length

        self.assertEqual(max_length_name, 200)
        self.assertEqual(product.name, 'Name')

    def test_product_str(self):
        product = models.Product.objects.get(article='09235')

        self.assertEqual(
            str(product),
            f'09235 | Name'
        )

    def test_product_author(self):
        product = models.Product.objects.get(article='09235')
        self.assertTrue(product.author)

    def test_product_created(self):
        product = models.Product.objects.get(article='09235')
        self.assertTrue(product.created)


