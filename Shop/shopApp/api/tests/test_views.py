import django
django.setup()

from django.test import TestCase
from shopApp import models
from django.contrib.auth.models import User


class ApiTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User(username='test_user')
        user.set_password('password')
        user.save()

        models.Product.objects.create(
            name='Name',
            article='09235',
            author=user
        )

    def test_api_products_get(self):
        resp = self.client.get('/api/products')

        self.assertEqual(resp.status_code, 200)

    def test_api_products_post_no_login(self):
        resp = self.client.post('/api/products')

        self.assertEqual(resp.status_code, 401)



    def test_api_products_post_login(self):
        self.client.login(username='test_user', password='password')
        resp = self.client.post('/api/products')

        self.assertEqual(resp.status_code, 400)

    def test_api_products_post(self):
        self.client.login(username='test_user', password='password')
        resp = self.client.post('/api/products',
                                data={
                                    'name': 'test_q',
                                    'article': '123456'}
                                )

        self.assertEqual(resp.status_code, 201)

    def test_api_products_get_one(self):
        resp = self.client.get('/api/products/09235')

        self.assertEqual(resp.status_code, 200)

    def test_api_products_patch_one(self):
        self.client.login(username='test_user', password='password')
        resp = self.client.patch('/api/products/09235', data={
            'name': 'changename'
        })

        product = models.Product.objects.get(article='09235')

        self.assertEqual(product.name, 'changename')
        self.assertEqual(resp.status_code, 200)


