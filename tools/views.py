from django.views.generic import ListView, DetailView
from .models import Application, Parameter


# class ToolsList(TemplateView):
#     template_name = 'tools/list.html'


class ToolsList(ListView):
    model = Application
    context_object_name = 'tools_list'
    template_name = 'tools/list.html'


class ToolsDetail(DetailView):
    model = Application
    context_object_name = 'application'
    template_name = 'tools/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ToolsDetail, self).get_context_data(**kwargs)

        context.update({
            'page_name': 'search_faq_list',
            'section_title_faq': {'title': 'FAQ一覧', 'sub_text': 'よくある質問の一覧です。', 'english_title': 'FAQ LIST'},
            'parameter_list': Parameter.objects.filter(application=self.kwargs['pk'])
        })
        return context