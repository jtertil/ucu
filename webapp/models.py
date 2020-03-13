from django.db import models


class ShortCut(models.Model):
    url = models.URLField(
        max_length=2000,
        help_text='Please use the following format: https://www.jmr.pl',
    )
