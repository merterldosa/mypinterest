# articleapp/forms.py 작성
from django import forms
from django.forms import ModelForm
from articleapp.models import Article
from projectapp.models import Project


class ArticleCreationForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable text-start',
                                                           'style': 'height: auto;'}))

    project = forms.ModelChoiceField(queryset=Project.objects.all())
    class Meta:
        model = Article
        fields = ['title', 'image', 'project', 'content'] # writer 는 서버 내에서 설정해줄 것이므로 제외