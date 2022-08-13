from django.views.generic import DetailView, ListView, CreateView
from .models import Article, Tag, Request
from .forms import RequestForm
from django.urls import reverse_lazy


class ArticleList(ListView):
    model = Article
    paginate_by = 10
    template_name = 'faq/list.html'
    context_object_name = 'faq_list'

    def get_context_data(self, **kwargs):
        context = super(ArticleList, self).get_context_data(**kwargs)
        context.update({
            'section_title_faq': {'title': 'FAQ一覧', 'sub_text': 'よくある質問の一覧です。', 'english_title': 'FAQ LIST'},
            'Tags': Tag.objects.all(),
        })
        return context


class ArticleDetail(DetailView):
    model = Article
    template_name = 'faq/detail.html'
    context_object_name = 'faq'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetail, self).get_context_data(**kwargs)
        context.update({
            'form': RequestForm
        })
        return context


class RequestCreate(CreateView):
    model = Request
    form_class = RequestForm
    template_name = 'faq/detail.html'
    context_object_name = 'contents_list'
    success_url = reverse_lazy('index')

    def save(self):
        data = self.cleaned_data
        post = Request(
            name=data['name'],
            email=data['email'],
            message=data['message'],
        )
        post.save()
