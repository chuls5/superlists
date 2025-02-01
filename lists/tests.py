from django.test import TestCase


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertContains(response, 'A new list item')
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_displays_posted_item(self):
        response = self.client.post('/', data={'item_text': 'Test item'})
        self.assertEqual(response.context['new_item_text'], 'Test item')
        self.assertContains(response, 'Test item')
