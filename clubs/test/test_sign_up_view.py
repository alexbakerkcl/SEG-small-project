"test of sign up view"
from django.test import TestCase
from clubs.forms import SignupForm
from django.urls import reverse
from clubs.models import User
from django.contrib.auth.hashers import check_password

class SignUpViewTestCase(TestCase):

     def setUp(self):
         self.url = reverse('signup')
         self.form_input = {
           'first_name': 'Jane',
           'last_name': 'Doe',
           'username': '@janedoe',
           'email': 'janedoe@example.org',
           'bio': 'My bio',
           'statement':'lol',
           'new_password': 'Password123',
           'password_confirmation': 'Password123'
          }

     def test_get_sign_up_url(self):
         self.assertEqual(reverse('signup'),'/signup/')

     def test_get_sign_up(self):
         url = reverse('signup')
         response = self.client.get(url)
         self.assertEqual(response.status_code, 200)
         self.assertTemplateUsed(response,'signup.html')
         form = response.context['form']
         self.assertTrue(isinstance(form,SignupForm))
         self.assertFalse(form.is_bound)

     def test_unsuccessful_sign_up(self):
         self.form_input['username'] = 'BAD_USERNAME'
         before_count = User.objects.count()
         response = self.client.post(self.url, self.form_input)
         after_count = User.objects.count()
         self.assertEqual(after_count,before_count)
         self.assertEqual(response.status_code, 200)
         self.assertTemplateUsed(response,'signup.html')
         form = response.context['form']
         self.assertTrue(isinstance(form,SignupForm))
         self.assertTrue(form.is_bound)

     def test_successful_sign_up(self):
         before_count = User.objects.count()
         response = self.client.post(self.url, self.form_input, follow=True)
         after_count = User.objects.count()
         self.assertEqual(after_count,before_count+1)
         response_url = reverse('feed')
         self.assertRedirects(response, response_url, status_code = 302, target_status_code = 200)
         self.assertTemplateUsed(response,'feed.html')
         user = User.objects.get(username='@janedoe')
         self.assertEqual(user.first_name, 'Jane')
         self.assertEqual(user.last_name, 'Doe')
         self.assertEqual(user.email, 'janedoe@example.org')
         self.assertEqual(user.bio, 'My bio')
         is_password_correct = check_password('Password123', user.password)
         self.assertTrue(is_password_correct)
