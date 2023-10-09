from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from web.models import Profile
from web.views import ProfileListView


class ProfilesListViewTests(TestCase):
    def test_get__expect_correct_template(self):
        response = self.client.get(reverse('list profiles'))

        self.assertTemplateUsed(response, 'profiles/list.html')

    def test_get__when_two_profile__expect_context_to_contain_two_profiles(self):
        # Arrange
        profiles_to_create = (
            Profile(first_name='Bogi',
                    last_name='Bak',
                    age=15),
            Profile(first_name='Baki',
                    last_name='Bogev',
                    age=81),
        )
        Profile.objects.bulk_create(profiles_to_create)

        # Act
        response = self.client.get(reverse('list profiles'))

        # Asset
        profiles = response.context['object_list']

        # Check for actual profiles
        self.assertEqual(len(profiles), 2)

    def test_get__when_not_logged_in_user__expect_context_user_to_be_No_user(self):
        response = self.client.get(reverse('list profiles'))
        self.assertEqual(
            ProfileListView.no_logged_in_user_value,
            response.context[ProfileListView.context_user_key]
        )

    def test_get__when_not_logged_in_user__expect_context_user_to_username(self):
        user_data = {
            'username': 'Bogi',
            'password': 'Bogi123',
        }

        UserModel = get_user_model()
        UserModel.objects.create_user(**user_data)
        self.client.login(**user_data)
        response = self.client.get(reverse('list profiles'))

        self.assertEqual(
            user_data['username'],
            response.context[ProfileListView.context_user_key]
        )

