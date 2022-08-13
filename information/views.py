from django.views.generic import DetailView, ListView
from .models import Article, Tag
from faq.models import Article as Faq


class ArticleList(ListView):
    model = Article
    paginate_by = 10
    context_object_name = 'information_list'
    template_name = 'information/list.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleList, self).get_context_data(**kwargs)
        context.update({
            'Tags': Tag.objects.all(),
            'faq_list': Faq.objects.all(),
        })
        return context


class ArticleDetail(DetailView):
    model = Article
    template_name = 'information/detail.html'
    context_object_name = 'information'
