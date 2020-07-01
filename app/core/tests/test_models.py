from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


def sample_user(email='test@hello.com', password='pass1234'):
    """to create a sample user for testing"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """test if creating a new user with an email is successful"""
        email = 'hello@people.com'
        password = 'PasstheTest'
        user = get_user_model().objects.create_user(email, password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test if the new user's email id is normalized"""
        email = 'test@HELLO.COM'
        user = get_user_model().objects.create_user(email, 'test562')

        self.assertEqual(user.email, email.lower())

    def test_new_user_email_validity(self):
        """test if the new user has an email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'testpw')

    def test_create_new_superuser(self):
        """ test creating a new superuser"""
        user = get_user_model().objects.create_superuser('sup@user.com', 'pas')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """test if tag is in string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='vegan'
        )

        self.assertEqual(str(tag), tag.name)
