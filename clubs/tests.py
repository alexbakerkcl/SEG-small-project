from django.test import TestCase
from .models import User
from django.core.exceptions import ValidationError

class UserModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            '@johndoe',
            experience = 'N',
            statement = 'I am new to Chess',
            bio='My name is John and I would like to practise and improve my chess skills.'
        )

    def test_valid_user(self):
        self._assert_user_is_valid()

    def _assert_user_is_valid(self):
        try:
            self.user.full_clean()
        except (ValidationError):
            self.fail('Test user should be valid')

    def _assert_user_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.user.full_clean()

    def _create_second_user(self):
        user = User.objects.create_user(
            '@alicesmith',
            experience='A',
            statement = 'I play Chess often',
            bio = 'I am from America and I enjoy playing Chess'

        )
