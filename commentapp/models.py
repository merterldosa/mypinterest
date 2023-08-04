from django.contrib.auth.models import User
from django.db import models

from articleapp.models import Article

# Create your models here.

class Comment(models.Model):
    # article, writer 둘 다 서버단에서 확인을 하기 위해 추가적인 hidden input 을 추가해야한다.
    # -> create.html 에 <input type="hidden" name="article_pk" value=""> 부분 추가
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True, related_name='comment')
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comment')

    content = models.TextField(null=False)  # content 는 입력을 받을 것

    created_at = models.DateTimeField(auto_now=True)    # created_at 은 자동으로 생성될 것