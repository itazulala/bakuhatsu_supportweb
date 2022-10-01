from django.shortcuts import render
from django.views.generic import View, ListView
from markdown import markdown

from contents.models import Article as Contents
from faq.models import Article as Faq
from information.models import Article as Information


class TopPage(ListView):
    model = Contents
    queryset = Information.objects.all()[:3]
    template_name = 'index.html'
    context_object_name = 'information_list'

    def get_context_data(self, **kwargs):
        context = super(TopPage, self).get_context_data(**kwargs)
        context.update({
            'top_flag': True,
            'section_title_faq': {'title': '最新FAQ', 'sub_text': '新着のよくある質問です。', 'english_title': 'PICKUP FAQ'},
            'faq_list': Faq.objects.all()[:5],
            'section_title_contents': {'title': '最新コンテンツ', 'sub_text': '新着のコンテンツです。', 'english_title': 'PICKUP CONTENTS'},
            'contents_list': Contents.objects.all().filter(draft=False)[:5]
        })
        return context


class PrivacyPolicy(View):
    def get(self, request):
        with open('templates/privacy-policy/privacy_policy_supportweb.md') as file:
            s = file.read()
        s_to_html = markdown(s)
        return render(request, 'privacy-policy/privacy-policy.html', context={'contents': s_to_html})
