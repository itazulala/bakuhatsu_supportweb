from django.views.generic import DetailView, ListView
from .models import Article, Tag


class ArticleDetail(DetailView):
    model = Article
    template_name = 'contents/detail.html'


class ArticleList(ListView):
    model = Article
    paginate_by = 10
    queryset = Article.objects.all().filter(draft=False)
    template_name = 'contents/list.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleList, self).get_context_data(**kwargs)
        context.update({
            'Tags': Tag.objects.all(),
        })
        return context

    




