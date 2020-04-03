from django.db import models

from .helpers import converter


class ShortCut(models.Model):

    url = models.URLField(
        max_length=2000,
        help_text='Please use the following format: https://www.google.com',
    )

    def pk_encode(self):
        return converter.encode(self.pk)

    def pk_decode(self, s):
        return converter.decode(s)
