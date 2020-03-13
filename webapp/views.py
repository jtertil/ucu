from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .helpers import converter, BASE_SYMBOLS
from .models import ShortCut
from .forms import UrlInputForm


def index(request):
    form = UrlInputForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        new_url = form.save()
        encoded = new_url.pk_encode()
        short = request.build_absolute_uri(f'/{encoded}')
        saving = len(new_url.url) - len(short)
        return render(request, 'webapp/index.html', {
            'short': short, 'saving': saving})
    else:
        form = UrlInputForm()
        return render(request, 'webapp/index.html', {'form': form})


def shortcut(request, s):
    """
    checks if all characters of input string are in the BASE_SYMBOLS
    decode primary key from input string
    redirects to url if exist, otherwise rise 404
    """
    b_symbols = set(BASE_SYMBOLS)
    s_symbols = set(s)
    if b_symbols.issuperset(s_symbols):
        url_pk = converter.decode(s)
        url = get_object_or_404(ShortCut, pk=url_pk).url
        return HttpResponseRedirect(url)
    else:
        raise Http404()
