"test of log in view"
from django.test import TestCase
from clubs.forms import LogInForm
from django.urls import reverse
from clubs.models import User
from .helpers import LogInTester

class LogInViewTestCase(TestCase, LogInTester):

     def setUp(self):
         self.url = reverse('login')
         User.objects.create_user('@johndoe',
             first_name='John',
             last_name='Doe',
             email='johndoe@example.org',
             bio='Hello, I am John Doe.',
             password='Password123',
         )

     def test_log_in_url(self):
         self.assertEqual(self.url,'/login/')

     def test_get_log_in(self):
         response = self.client.get(self.url)
         self.assertEqual(response.status_code, 200)
         self.assertTemplateUsed(response,'login.html')
         form = response.context['form']
         self.assertTrue(isinstance(form,LogInForm))
         self.assertFalse(form.is_bound)

     def test_unsuccesful_log_in(self):
        form_input = { 'username': '@johndoe' , 'password' : 'WrongPassword123'}
        response = self.client.post(self.url,form_input)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'login.html')
        form = response.context['form']
        self.assertTrue(isinstance(form,LogInForm))
        self.assertFalse(form.is_bound)
        self.assertFalse(self._is_logged_in())

     def test_succesful_log_in(self):
         form_input = { 'username': '@johndoe', 'password': 'Password123' }
         response = self.client.post(self.url, form_input, follow=True)
         self.assertTrue(self._is_logged_in())
         response_url = reverse('feed')
         self.assertRedirects(response, response_url, status_code = 302, target_status_code = 200)
         self.assertTemplateUsed(response,'feed.html')
