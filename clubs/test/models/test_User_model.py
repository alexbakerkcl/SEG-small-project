from django.test import TestCase
from clubs.models import User
from django.core.exceptions import ValidationError

class UserModelTestCase(TestCase):

    fixtures = ['clubs/test/fixtures/default_user.json',
                'clubs/test/fixtures/other_users.json'
    ]

    def setUp(self):
        self.user = User.objects.get(username = '@johndoe')

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


    def test_username_cannot_be_blank(self):
        self.user.username = ''
        self._assert_user_is_invalid()

    def test_username_can_be_30_characters_long(self):
        self.user.username = '@' + 'x' * 29
        self._assert_user_is_valid()

    def test_username_cannot_be_over_30_characters_long(self):
        self.user.username = '@' + 'x' * 30
        self._assert_user_is_invalid()

    def test_username_must_be_unique(self):
        second_user = User.objects.get(username = '@janedoe')
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


    def test_valid_experience_levele(self):
        self.user.experience = 'E'
        self._assert_user_is_valid()

    def test_valid_experience_levela(self):
        self.user.experience = 'A'
        self._assert_user_is_valid()

    def test_valid_experience_leveli(self):
        self.user.experience = 'I'
        self._assert_user_is_valid()

    def test_valid_experience_levelb(self):
        self.user.experience = 'B'
        self._assert_user_is_valid()

    def test_valid_experience_leveln(self):
        self.user.experience = 'N'
        self._assert_user_is_valid()


    def test_statement_can_be_blank(self):
        self.user.statement = ''
        self._assert_user_is_valid()

    def test_statement_can_be_520_characters_long(self):
        self.user.statement = 'x' * 520
        self._assert_user_is_valid()

    def test_statement_cannot_be_over_520_characters_long(self):
        self.user.statement = 'x' * 521
        self._assert_user_is_invalid()

    def test_statement_may_contain_numbers(self):
        self.user.statement = 'statement 2'
        self._assert_user_is_valid()


    def test_bio_can_be_blank(self):
        self.user.bio = ''
        self._assert_user_is_valid()

    def test_bio_can_be_520_characters_long(self):
        self.user.bio = 'x' * 520
        self._assert_user_is_valid()

    def test_bio_cannot_be_over_520_characters_long(self):
        self.user.bio = 'x' * 521
        self._assert_user_is_invalid()

    def test_bio_may_contain_numbers(self):
        self.user.bio = 'bio 2'
        self._assert_user_is_valid()

    def test_toggle_follow_user(self):
        jane = User.objects.get(username='@janedoe')
        self.assertFalse(self.user.is_following(jane))
        self.assertFalse(jane.is_following(self.user))
        self.user.toggle_follow(jane)
        self.assertTrue(self.user.is_following(jane))
        self.assertFalse(jane.is_following(self.user))
        self.user.toggle_follow(jane)
        self.assertFalse(self.user.is_following(jane))
        self.assertFalse(jane.is_following(self.user))

    def test_follow_counters(self):
        jane = User.objects.get(username='@janedoe')
        petra = User.objects.get(username='@petrapickles')
        peter = User.objects.get(username='@peterpickles')
        self.user.toggle_follow(jane)
        self.user.toggle_follow(petra)
        self.user.toggle_follow(peter)
        jane.toggle_follow(petra)
        jane.toggle_follow(peter)
        self.assertEqual(self.user.follower_count(), 0)
        self.assertEqual(self.user.followee_count(), 3)
        self.assertEqual(jane.follower_count(), 1)
        self.assertEqual(jane.followee_count(), 2)
        self.assertEqual(petra.follower_count(), 2)
        self.assertEqual(petra.followee_count(), 0)
        self.assertEqual(peter.follower_count(), 2)
        self.assertEqual(peter.followee_count(), 0)

    def test_user_cannot_follow_self(self):
        self.user.toggle_follow(self.user)
        self.assertEqual(self.user.follower_count(), 0)
        self.assertEqual(self.user.followee_count(), 0)
