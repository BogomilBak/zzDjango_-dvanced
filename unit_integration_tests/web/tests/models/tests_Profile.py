from unittest import TestCase

from django.core.exceptions import ValidationError
from django.test import TestCase as DTestCase

from web.models import Profile
import django

django.setup()


class ProfileTests(DTestCase):
    VALID_USER_DATA = {
        'first_name': 'Bogi',
        'last_name': 'Bak',
        'age': 15,
    }

    def test_profile_create__when_first_name_contains_only_letters__expect_success(self):
        profile = Profile(**self.VALID_USER_DATA)
        profile.save()
        self.assertIsNotNone(profile.pk)

    def test_profile_create__when_first_name_contains_a_digit__expect_to_fail(self):
        first_name = 'Bog1'
        profile = Profile(
            first_name=first_name,
            last_name=self.VALID_USER_DATA['last_name'],
            age=self.VALID_USER_DATA['age'],
        )
        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)

    def test_profile_create__when_first_name_contains_a_dollar_sign_expect_to_fail(self):
        first_name = 'Bo$g'
        profile = Profile(
            first_name=first_name,
            last_name=self.VALID_USER_DATA['last_name'],
            age=self.VALID_USER_DATA['age'],
        )
        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)

    def test_profile_create__when_first_name_contains_a_space__expect_to_fail(self):
        first_name = 'Bo g1'
        profile = Profile(
            first_name=first_name,
            last_name=self.VALID_USER_DATA['last_name'],
            age=self.VALID_USER_DATA['age'],
        )
        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)

    def test_profile_full_name__when_valid__expect_correct_full_name(self):
        profile = Profile(
            first_name='Bogi',
            last_name='Bak',
            age=15,
        )
        expected_full_name = f"{self.VALID_USER_DATA['first_name']} {self.VALID_USER_DATA['last_name']}"
        self.assertEqual(expected_full_name, profile.full_name)
