from django.test import TestCase


class IndexViewTest(TestCase):

    def test_index_response(self):
        r = self.client.get('/')
        self.assertEqual(r.status_code, 200)


class ShortcutViewTest(TestCase):

    def test_shortcut_response(self):
        pass

    def test_shortcut_response_invalid(self):
        pass

    def test_shortcut_decode_pk(self):
        pass

