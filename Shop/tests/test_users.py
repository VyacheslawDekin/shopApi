from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import reverse


class UserLoginTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User(username='test_user')
        user.set_password('password')
        user.save()




