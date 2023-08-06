from django.contrib.auth.models import User
from django.db import models

from projectapp.models import Project


# Create your models here.

class Subscription(models.Model):
    # 유저 연결
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscription')
    # 프로젝트 연결
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='subscription')

    class Meta: # Meta 정보로 넘겨주기
        # 어떤 유저와 어떤 프로젝트 그 쌍이 가지는 구독 정보가 단 하나가 되도록 설정.
        unique_together = ('user', 'project')