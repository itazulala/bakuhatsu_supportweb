from django.forms import ModelForm, TextInput, Textarea, HiddenInput
from .models import Thread, Comment
from django.core.validators import validate_email


class ThreadForm(ModelForm):

    class Meta:
        model = Thread
        fields = ['article', 'name', 'email', 'message']
        widgets = {
            'article': HiddenInput(),
            'name': TextInput(attrs={'placeholder': '氏名/ニックネームを入力してください。'}),
            'email': TextInput(attrs={'placeholder': 'メールアドレスを入力してください。'}),
            'message': Textarea(attrs={'cols': 1, 'rows': 15})
        }


class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ['thread', 'admin_flag', 'name', 'email', 'message']
        widgets = {
            'thread': HiddenInput(),
            'admin_flag': HiddenInput(),
            'name': TextInput(attrs={'placeholder': '氏名/ニックネームを入力してください。'}),
            'email': TextInput(attrs={'placeholder': 'メールアドレスを入力してください。'}),
            'message': Textarea(attrs={'cols': 1, 'rows': 15})
        }

