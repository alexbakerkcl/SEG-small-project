"unit test of the log in test_form_must_save_correctly"
from django.test import TestCase
from django import forms
from clubs.forms import LogInForm

class LogInFormTestCase(TestCase):

  def setUp(self):
      self.form_input = {'username': '@janedoe', 'password': 'Password123'}

  def test_form_contain_requid_fields(self):
      form = LogInForm()
      self.assertIn('username',form.fields)
      self.assertIn('password',form.fields)
      password_field = form.fields['password']
      self.assertTrue(isinstance(password_field.widget,forms.PasswordInput))

  def test_form_accepts_valid_input(self):
      form = LogInForm(data=self.form_input)
      self.assertTrue(form.is_valid())

  def test_form_rejects_blank_username(self):
      self.form_input['username'] = ''
      form = LogInForm(data=self.form_input)
      self.assertFalse(form.is_valid())

  def test_form_rejects_blank_password(self):
      self.form_input['password'] = ''
      form = LogInForm(data=self.form_input)
      self.assertFalse(form.is_valid())

  def test_form_accepts_incorrect_username(self):
      self.form_input['username'] = 'ja'
      form = LogInForm(data=self.form_input)
      self.assertTrue(form.is_valid())

  def test_form_accepts_incorrect_password(self):
      self.form_input['password'] = 'pwd'
      form = LogInForm(data=self.form_input)
      self.assertTrue(form.is_valid())
