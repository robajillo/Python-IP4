import unittest
from app.models import User
from app import db

class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_user = User(username='roba',email='rjillo@59@gmail.com',password = 'access')

    def test_password_setter(self):
        self.assertTrue(self.new_user.password_hash is not None)

    def test_no_access_password(self):
            with self.assertRaises(AttributeError):
                self.new_user.password

    def test_password_verification(self):
            self.assertTrue(self.new_user.verify_password('access'))