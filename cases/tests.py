from django.urls import resolve, reverse
from django.test import Client, TestCase
class HomePageTest(TestCase):
   def setUp(self):
      self.client = Client()
   def test_root_url_resolves_to_home_page_view(self):
      found = resolve('/')
      self.assertEqual(found.view_name, 'cases:home_page') 
      self.client 
   def test_home_page_returns_correct_html(self):
      response = self.client.get(reverse('cases:home_page'))
      self.assertTrue(response)