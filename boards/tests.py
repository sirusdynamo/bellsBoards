from django.test import TestCase
from django.urls import reverse, resolve
from .views import home
# Create your tests here.


class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url=reverse('home')
        response =self.client.get(url)
        self.assertEqual(response.status_code, 200)



    def test_home_url_resolves_home(self):
        view = resolve('/')
        self.assertEqual(view.func ,home)

    def test_home_resolves_home_url_name(self):
        view =resolve('/')
        self.assertEqual(view.url_name,'home')