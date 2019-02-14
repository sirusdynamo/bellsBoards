from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .views import signup
# Create your tests here.


class SignUpTest(TestCase):

    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)


    def test_signup_url_test_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_signup_url_resolves_signup_view(self):
        view = resolve('/signup/')
        self.assertEqual(view.func, signup)

    def test_csrftoken(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, UserCreationForm)


class SucessfulSignUpTest(TestCase):
    def setUp(self):
        url = reverse('signup')
        data= {
            'username':'sarah',
            'password1':'abcde1234',
            'password2':'abcde1234'
                    }
        self.response = self.client.post(url, data)
        self.home_url = reverse('home')

    def test_redirection(self):
        self.assertRedirects(self.response, self.home_url)


    def test_user_creation_successful(self):
        self.assertTrue(User.objects.exists())

    def test_user_authentication(self):
        response = self.client.get(self.home_url)
        user = response.context.get('user')
        self.assertTrue(user.is_authenticated)


class InvalidSignUptest(TestCase):
    def setUp(self):
        url = reverse('signup')
        data ={}
        self.response = self.client.post( url, data)
        

    def test_signup_status_code(self):
        self.assertEqual(self.response.status_code ,200)

    def test_form_errors(self):
        form = self.response.context.get('form')
        self.assertTrue(form.errors)        

    def test_dont_create_user(self):
        self.assertFalse(User.objects.exists())