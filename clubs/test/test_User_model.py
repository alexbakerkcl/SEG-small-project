from django.test import TestCase
from clubs.models import User
from django.core.exceptions import ValidationError

class UserModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            '@johndoe',
            #experience = 'N',
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
        #    experience='A',
            statement = 'I play Chess often',
            bio = 'I am from America and I enjoy playing Chess'

        )

    def test_username_cannot_be_blank(self):
        self.user.username = ''
        self._assert_user_is_invalid()

    def test_username_can_be_40_characters_long(self):
        self.user.username = '@' + 'x' * 39
        self._assert_user_is_valid()

    def test_username_cannot_be_over_40_characters_long(self):
        self.user.username = '@' + 'x' * 40
        self._assert_user_is_invalid()

    def test_username_must_be_unique(self):
        second_user = self._create_second_user()
        self.user.username = second_user.username
        self._assert_user_is_invalid()

    def test_username_must_start_with_at_symbol(self):
        self.user.username = 'johndoe'
        self._assert_user_is_invalid()

    def test_username_must_contain_at_least_3_alphanumericals_after_at(self):
        self.user.username = '@jo'
        self._assert_user_is_invalid()

    def test_username_must_contain_only_alphanumericals_after_at(self):
        self.user.username = '@john!doe'
        self._assert_user_is_invalid()

    def test_username_may_contain_numbers(self):
        self.user.username = '@j0hndoe2'
        self._assert_user_is_valid()

    def test_username_may_contain_only_one_at(self):
        self.user.username = '@@johndoe'
        self._assert_user_is_invalid()
