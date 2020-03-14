from django.forms import ModelForm

from .models import ShortCut


class UrlInputForm(ModelForm):
    class Meta:
        model = ShortCut
        fields = ('url', )
