from django.views.generic import DetailView, ListView, CreateView
from .models import Article, Tag, Request
from .forms import RequestForm
from django.urls import reverse_lazy
from django.db.models import Q


class ArticleList(ListView):
    model = Article
    paginate_by = 10
    ordering = '-created_at'
    template_name = 'faq/list.html'
    context_object_name = 'faq_list'

    def get_context_data(self, **kwargs):
        context = super(ArticleList, self).get_context_data(**kwargs)
        context.update({
            'page_name': 'search_faq_list',
            'section_title_faq': {'title': 'FAQ一覧', 'sub_text': 'よくある質問の一覧です。', 'english_title': 'FAQ LIST'},
            'tag_list': Tag.objects.all(),
        })
        return context


class ArticleSearchList(ListView):
    model = Article
    paginate_by = 10
    ordering = '-created_at'
    template_name = 'faq/list.html'
    context_object_name = 'faq_list'

    def get_queryset(self):
        queryset = Article.objects.order_by('-created_at')
        keyword = self.request.GET.get('keyword')
        tag = self.request.GET.get('tag')
        print(keyword)
        print(tag)
        if keyword:
            queryset = Article.objects.filter(
                Q(title__icontains=keyword) |
                Q(content__icontains=keyword) |
                Q(tags__in=Tag.objects.filter(name__icontains=keyword))
            )

        if tag:
            queryset = Article.objects.filter(
                tags__in=Tag.objects.filter(name__iexact=tag)
            )
        print(queryset)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ArticleSearchList, self).get_context_data(**kwargs)

        context.update({
            'page_name': 'search_faq_list',
            'section_title_faq': {'title': 'FAQ一覧', 'sub_text': 'よくある質問の一覧です。', 'english_title': 'FAQ LIST'},
            'tag_list': Tag.objects.all
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
