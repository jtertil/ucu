from unittest import skip

from django.db import IntegrityError, DataError
from django.test import TestCase

from .models import ShortCut


class ShortCutTest(TestCase):

    valid_url = 'https://www.jmr.pl'
    long_url = 'https://www.google.com/search?client=ubuntu&hs=9sT&channel=' \
               'fs&q=Pneumonoultramicroscopicsilicovolcanoconiosis&spell=' \
               '1&sa=X&ved=2ahUKEwj3wra805foAhWxtYsKHexcBH4QBSgAegQIEBAq'
    toolong_url = f'https//www.{"a" * 4000}.com'
    null_url = None
    invalid_url = 'somestring'

    def test_create_shortcut_valid_url(self):
        s = ShortCut.objects.create(url=self.valid_url)
        self.assertTrue(isinstance(s, ShortCut))

    def test_create_shortcut_long_url(self):
        s = ShortCut.objects.create(url = self.long_url)
        self.assertTrue(isinstance(s, ShortCut))

    @skip('SQLite does not enforce the length of a VARCHAR')
    def test_create_shortcut_url_toolong(self):
        s = ShortCut.objects.create
        self.assertRaises(DataError, s, url=self.toolong_url)

    def test_create_shortcut_null_url(self):
        s = ShortCut.objects.create
        self.assertRaises(IntegrityError, s, url=self.null_url)

    def test_create_shortcut_queries_num(self):
        s = ShortCut.objects.create
        self.assertNumQueries(1, s, url=self.valid_url)

    def test_get_or_create_shortcut_queries_num(self):
        s = ShortCut.objects.get_or_create
        self.assertNumQueries(4, s, url=self.valid_url)

    @skip('Still looking for best way to store URL in db.')
    def test_create_shortcut_url_invalid(self):
        s = ShortCut.objects.create
        self.assertRaises(DataError, s, url=self.invalid_url)

    def test_shortcut_pk_encode(self):
        pass

    def test_shortcut_pk_decode(self):
        pass
