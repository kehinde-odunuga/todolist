from rest_framework.test import APITestCase
from authentication.models import User


class TestModel(APITestCase):
    
    def test_creates_user(self):
        user = User.objects.create_user('Chris',  'chris@yopmail.com', 'Password123#')
        self.assertIsInstance(user, User)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email, 'chris@yopmail.com')

    def test_username_is_blank(self):
        self.assertRaises(ValueError, User.objects.create_user, username='', email='chris@yopmail.com', password='Password123#')

    def test_username_is_blank_with_error_message(self):
        with self.assertRaisesMessage(ValueError, 'The given username must be set'):
            User.objects.create_user(username='', email='chris@yopmail.com', password='Password123#')

    def test_email_is_blank(self):
        self.assertRaises(ValueError, User.objects.create_user, username='Chris', email='', password='Password123#')
        self.assertRaisesMessage(ValueError, 'The given email must be set')

    def test_email_is_blank_with_error_message(self):
        with self.assertRaisesMessage(ValueError, 'The given email must be set'):
            User.objects.create_user(username='Chris', email='', password='Password123#')

    def test_creates_super_user(self):
        user = User.objects.create_superuser('Admin',  'admink@yopmail.com', 'Password123#')
        self.assertIsInstance(user, User)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.email, 'admink@yopmail.com')

    def test_username_is_blank_with_error_message(self):
        with self.assertRaisesMessage(ValueError, 'The given username must be set'):
            User.objects.create_user(username='', email='chris@yopmail.com', password='Password123#')

    
    def test_creates_super_user_with_staff_status(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_staff=True.'):
            User.objects.create_superuser(username='Admin', email='admink@yopmail.com', password='Password123#', is_staff=False)

    def test_creates_super_user_with_super_user_status(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_superuser=True.'):
            User.objects.create_superuser(username='Admin', email='admink@yopmail.com', password='Password123#', is_superuser=False)