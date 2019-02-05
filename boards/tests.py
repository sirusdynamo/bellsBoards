from django.test import TestCase
from django.urls import reverse, resolve
from .views import home , board_topics
from .models import Board
# Create your tests here.


class HomeTests(TestCase):
    def setUp(self):
        self.board =Board.objects.create(name='Django', description='Django boards ')
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        self.assertEqual(self.response.status_code, 200)


    def test_home_url_resolves_home(self):
        view = resolve('/')
        self.assertEqual(view.func ,home)

    def test_home_resolves_home_url_name(self):
        view =resolve('/')
        self.assertEqual(view.url_name,'home')

    def test_home_view_contains_link_to_topics_page(self):
        board_topics_url = reverse('board_topics', kwargs={'board_id': self.board.pk})
        self.assertContains(self.response, 'href="{0}"'.format(board_topics_url))



class BoardTopicsTest(TestCase):

    def setUp(self):
        Board.objects.create(name='Django', description='A discusion about django')


    def test_board_topics_success_status_code(self):
        url = reverse('board_topics', kwargs={'board_id':1})
        response =self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_board_topics_view_not_found_status_code(self):
        url = reverse('board_topics', kwargs= {'board_id':89})
        response =self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_board_topics_url_resolves_board_topics_view_(self):
        view = resolve('/boards/1/')
        self.assertEqual(view.func ,board_topics)



