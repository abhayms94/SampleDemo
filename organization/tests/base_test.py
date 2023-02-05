from django.test import TestCase
from django.contrib.auth.models import User
from faker import Faker


class NewUserTestCase(TestCase):
    def setUp(self) -> None:
        faker = Faker()
        self.username = faker.user_name()
        self.password = faker.password()
        self.email = faker.email()
        self.firstname = faker.first_name()
        self.lastname = faker.last_name()
        self.user = User.objects.create_user(username=self.username,
                                             password=self.password,
                                             first_name=self.firstname,
                                             lastname=self.lastname)

    def tearDown(self) -> None:
        self.user.delete()
        