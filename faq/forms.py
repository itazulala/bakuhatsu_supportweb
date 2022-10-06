from django.forms import ModelForm, TextInput, Textarea
from .models import Request


class RequestForm(ModelForm):

    class Meta:
        model = Request
        fields = ['name', 'title', 'message']
        widgets = {
            'name': TextInput(attrs={'placeholder': '氏名/ニックネームを入力してください。'}),
            'title': TextInput(attrs={'placeholder': '件名を入力してください。'}),
            'message': Textarea(attrs={'placeholder': 'リクエスト内容を入力してください。', 'cols': 1, 'rows': 15})
        }
