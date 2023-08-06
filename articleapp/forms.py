# articleapp/forms.py 작성
from django.forms import ModelForm
from articleapp.models import Article


class ArticleCreationForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'image', 'project', 'content'] # writer 는 서버 내에서 설정해줄 것이므로 제외