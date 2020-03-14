from django.test import TestCase
from .models import ShortCut


class IndexViewTest(TestCase):

    def test_index_response(self):
        r = self.client.get('/')
        self.assertEqual(r.status_code, 200)


class ShortcutViewTest(TestCase):

    def setUp(self) -> None:
        self.s = ShortCut.objects.create(url='https://www.google.com')

    def test_shortcut_response(self):
        r = self.client.get(f'/{self.s.pk_encode()}')
        self.assertEqual(r.status_code, 302)

    def test_shortcut_response_invalid(self):
        r = self.client.get('/nonexistent')
        self.assertEqual(r.status_code, 404)

    def test_shortcut_prohibited_symbols(self):
        r = self.client.get('/ohnoprohibitedsymbols!')
        self.assertEqual(r.status_code, 404)
