from django.test import TestCase
from django.urls import reverse
from clubs.models import Club

class ClubListTest(TestCase):

    fixtures = [
        'clubs/test/fixtures/default_user.json',
        'clubs/test/fixtures/default_club.json'
    ]

    def setUp(self):
        self.response = self.client.get('', {'clubs':Clubs.objects.all()})


    def  test_clubs_content_contains_club(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, 'Alone')
        self.assertTemplateUsed(self.response, 'home.html')
