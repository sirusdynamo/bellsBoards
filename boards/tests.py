from django.test import TestCase
from django.urls import reverse, resolve
from .views import home , board_topics ,new_topics
from .models import Board
from .forms import NewTopicForm
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

    def test_home_view_contains_link_to_home_page(self):
        board_topics_url = reverse('board_topics', kwargs={'board_id': self.board.pk})
        homepage_url =reverse('home')
        self.response =self.client.get(board_topics_url)
        self.assertContains(self.response, 'href="{0}"'.format(homepage_url))



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

    def test_board_topics_view_contains_navigation_links(self):
        board_topics_url = reverse('board_topics', kwargs={'pk': 1})
        homepage_url = reverse('home')
        new_topic_url = reverse('new_topic', kwargs={'pk': 1})

        response = self.client.get(board_topics_url)

        self.assertContains(response, 'href="{0}"'.format(homepage_url))
        self.assertContains(response, 'href="{0}"'.format(new_topic_url))


    # def test


class NewTopicTests(TestCase):

    def setUp(self):
        Board.objects.create(name='Django', description='A discusion about django')

    def test_new_topics_success_status_code(self):
        url = reverse('new_topics', kwargs={'board_id':1})
        response =self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_new_topics_view_not_found_status_code(self):
        url = reverse('new_topics', kwargs= {'board_id':89})
        response =self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_new_topics_url_resolves_new_topics_view_(self):
        view = resolve('/boards/1/new/')
        self.assertEqual(view.func, new_topics)

    # def test_new(self):
    #     new_topics_url = reverse('new_topics', kwargs={'board_id':1})
    #     board_topics_url = reverse('board_topics', kwargs={'board_id':1})
    #     response= self.client.get(new_topics_url)
    #     self.assertContains(response, "href='{0}'".format(board_topics_url))


    def test_contains_form(self):
        url = reverse('new_topics', kwargs={'board_id': 1})
        response = self.client.get(url)
        form = response.context.get('form')
        self.assertIsInstance(form ,NewTopicForm)

    def test_new_topic_invalid_post(self):
        url = reverse('new_topics', kwargs={'board_id':1})
        response = self.client.post(url, {})
        form = response.context.get('form')

        self.assertEquals(response.status_code, 200)
        self.assertTrue(form.errors)

    def test_new_topic_valid_form(self):
        form = NewTopicForm({'subject': 'debugging', 'message':r'this the result of the tests'})
        self.assertTrue(form.is_valid())
        


    



