from django.views.generic import DetailView
from django.views.generic import ListView
from .models import Article


class ArticleDetail(DetailView):
    model = Article
    template_name = 'contents/detail.html'


class ArticleList(ListView):
    model = Article
    queryset = Article.objects.all().filter(draft=True)
    template_name = 'contents/list.html'




