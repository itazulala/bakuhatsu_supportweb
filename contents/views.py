from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView, CreateView, FormView
from .models import Article, Thread, Comment, Tag
from .forms import ThreadForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.contrib import messages


class ArticleDetail(DetailView, CreateView):
    model = Article
    template_name = 'contents/detail.html'
    form_class = ThreadForm
    success_url = '/'
    context_object_name = 'content'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetail, self).get_context_data(**kwargs)
        context['form'] = ThreadForm
        context.update({
            'thread_list': Thread.objects.filter(article=self.kwargs['pk']),
        })
        return context


class ArticleList(ListView):
    model = Article
    paginate_by = 10
    template_name = 'contents/list.html'
    context_object_name = 'contents_list'

    def get_context_data(self, **kwargs):
        context = super(ArticleList, self).get_context_data(**kwargs)
        context.update({
            'section_title_contents': {'title': 'コンテンツ一覧', 'sub_text': 'コンテンツ一覧です。', 'english_title': 'PICKUP CONTENTS'},
        })
        return context


class ThreadCreate(CreateView):
    model = Thread, Article
    form_class = ThreadForm
    template_name = 'contents/detail.html'

    def save(self):
        data = self.cleaned_data
        post = Thread(
            article=data['article'],
            name=data['name'],
            email=data['email'],
            message=data['message'],
        )
        post.save()

    def get_success_url(self):
        return reverse('contents_detail', kwargs={'pk': self.object.article.id})

    def form_invalid(self, form):
        content = Article.objects.filter(
            id=form.data['article']).values('title', 'content', 'created_at', 'tags')[0]
        context = self.get_context_data()
        context.update({
            'error_message': form.errors['email'],
            'content': {
                'title': content['title'],
                'content': content['content'],
                'created_at': content['created_at']
            }
        })
        print(context)
        return self.render_to_response(context)


class CommentCreate(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'contents/detail.html'

    def save(self):
        data = self.cleaned_data
        post = Comment(
            article=data['thread'],
            name=data['name'],
            email=data['email'],
            message=data['message'],
        )
        post.save()

    def get_success_url(self):
        return reverse('comment_detail', kwargs={'pk': self.object.thread.id})


class CommentDetail(DetailView):
    model = Thread
    template_name = 'contents/comment/detail.html'
    success_url = reverse_lazy('index')
    context_object_name = 'thread'

    def get_context_data(self, **kwargs):
        context = super(CommentDetail, self).get_context_data(**kwargs)
        context.update({
            'form': CommentForm,
            'section_title_contents': {'title': '質問/コメント', 'english_title': 'PICKUP CONTENTS'},
            'comment_list': Comment.objects.filter(thread=self.kwargs['pk']),
        })
        return context
