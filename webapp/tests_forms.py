from django.test import TestCase

from .forms import UrlInputForm


class InputFormTest(TestCase):
    valid_url = 'https://www.google.com'
    long_url = 'https://www.google.com/search?client=ubuntu&hs=9sT&channel=' \
               'fs&q=Pneumonoultramicroscopicsilicovolcanoconiosis&spell=' \
               '1&sa=X&ved=2ahUKEwj3wra805foAhWxtYsKHexcBH4QBSgAegQIEBAq'
    toolong_url = f'https//www.{"a" * 2000}.com'
    blank_url = ''
    invalid_url = 'somestring'

    def test_form_init(self):
        f = UrlInputForm()
        self.assertIsInstance(f, UrlInputForm)

    def test_form_with_valid_input(self):
        f = UrlInputForm({'url': self.valid_url})
        self.assertTrue(f.is_valid())

    def test_form_with_long_input(self):
        f = UrlInputForm({'url': self.long_url})
        self.assertTrue(f.is_valid())

    def test_form_with_toolong_input(self):
        f = UrlInputForm({'url': self.toolong_url})
        self.assertFalse(f.is_valid())
        self.assertEqual(f.errors, {
            'url': ['Enter a valid URL.',
                    'Ensure this value has at most 2000 characters'
                    ' (it has 2022).']
        })

    def test_form_with_invalid_input(self):
        f = UrlInputForm({'url': self.invalid_url})
        self.assertFalse(f.is_valid())
        self.assertEqual(f.errors, {
            'url': ['Enter a valid URL.']
        })

    def test_form_with_blank_input(self):
        f = UrlInputForm({'url': self.blank_url})
        self.assertFalse(f.is_valid())
        self.assertEqual(f.errors, {
            'url': ['This field is required.']
        })

