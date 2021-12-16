"test of log in view"
from django.test import TestCase
from clubs.forms import LogInForm
from django.urls import reverse
from clubs.models import User
from clubs.test.helpers import LogInTester
from django.contrib import messages

class LogInViewTestCase(TestCase, LogInTester):

     fixtures = ['clubs/test/fixtures/default_user.json']


     def setUp(self):
         self.url = reverse('login')
         self.user = User.objects.get(username = '@johndoe')

     def test_log_in_url(self):
         self.assertEqual(self.url,'/login/')

     def test_get_log_in(self):
         response = self.client.get(self.url)
         self.assertEqual(response.status_code, 200)
         self.assertTemplateUsed(response,'login.html')
         form = response.context['form']
         self.assertTrue(isinstance(form,LogInForm))
         self.assertFalse(form.is_bound)
        # messages_list = list(response.context['messages'])
        # self.assertTrue(len(messages_list),0)

     def test_unsuccesful_log_in(self):
        form_input = { 'username': '@johndoe' , 'password' : 'WrongPassword123'}
        response = self.client.post(self.url,form_input)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'login.html')
        form = response.context['form']
        self.assertTrue(isinstance(form,LogInForm))
        self.assertFalse(form.is_bound)
        self.assertFalse(self._is_logged_in())
        messages_list = list(response.context['messages'])
        self.assertTrue(len(messages_list),1)
        self.assertTrue(messages_list[0].level,messages.ERROR)

     def test_succesful_log_in(self):
         form_input = { 'username': '@johndoe', 'password': 'Password123' }
         response = self.client.post(self.url, form_input, follow=True)
         self.assertTrue(self._is_logged_in())
         response_url = reverse('feed')
         self.assertRedirects(response, response_url, status_code = 302, target_status_code = 200)
         self.assertTemplateUsed(response,'feed.html')
        # messages_list = list(response.context['messages'])
        # self.assertTrue(len(messages_list),0)

     def test_vaild_log_in_by_inactive_user(self):
          self.user.is_active = False
          self.user.save()
          form_input = { 'username': '@johndoe', 'password': 'Password123' }
          response = self.client.post(self.url, form_input, follow=True)
          self.assertEqual(response.status_code, 200)
          self.assertTemplateUsed(response,'login.html')
          form = response.context['form']
          self.assertTrue(isinstance(form,LogInForm))
          self.assertFalse(form.is_bound)
          self.assertFalse(self._is_logged_in())
          messages_list = list(response.context['messages'])
          self.assertTrue(len(messages_list),1)
          self.assertTrue(messages_list[0].level,messages.ERROR)
