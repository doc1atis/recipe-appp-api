from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


def sample_user(email='testolgy@yahoo.com', password='passsolgy23'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating a new user with email is sucessful"""
        email = "olgy@yahoo.com"
        password = "olgy1234"
        user = get_user_model().objects.create_user(email=email,
                                                    password=password
                                                    )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a user is normalized"""
        email = 'test@YAHOO.COM'
        user = get_user_model().objects.create_user(email=email,
                                                    password="edfre3"
                                                    )
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises an error"""
        with self.assertRaises(ValueError):
            # if this does not raise a ValueError the test will fail
            get_user_model().objects.create_user(None, "werfd32")

    def test_create_new_superuser(self):
        """Test creating a new super user"""
        user = get_user_model().objects.\
            create_superuser('test3@yahoo.com', 'wed54')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )
        self.assertEqual(str(tag), tag.name)
