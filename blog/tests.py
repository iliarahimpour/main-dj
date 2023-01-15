from django.test import TestCase , SimpleTestCase

# Create your tests here.


class SimpleTests(SimpleTestCase):
    def test_home_page(self):
        response=self.client.get('/')
        self.assertEqual(response.status_code, 200)
    def test_blog_page(self):
         response=self.client.get('/blog')
         self.assertEqual(response.status_code, 200)

