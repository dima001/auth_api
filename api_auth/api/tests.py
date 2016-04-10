from django.test import TestCase
from .models import User


class UserTest(TestCase):
    def create(self,first_name="dima",last_name="bro",email="dima@gmail.com"):
        return User.objects.create(first_name=first_name, last_name=last_name,email=email,username="dima1")

    def test_user_have_mail(self):
        user = self.create("dima","b","dima001@gmail.com")
        self.assertEqual(user.email, "dima001@gmail.com")