from django.views.generic import ListView
from django.views.generic import FormView
from faq.models import Article as faq
from contents.models import Article as contents


class TopPage(ListView):
    model = faq
    queryset = contents.objects.all().filter(draft=True)
    template_name = 'index.html'

    