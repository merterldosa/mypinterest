from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView, ListView

from articleapp.models import Article
from projectapp.models import Project
from subscribeapp.models import Subscription


# Create your views here.
# 로그인을 해야지 구독을 할 수 있도록 하기, 숨길건 없으므로 get 방식
@method_decorator(login_required, 'get')
class SubscriptionView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):

        # detail 안아서 구독 버튼을 누를 수 있도록 하기 위해 되 돌아갈 곳은 projectapp 에서 detail 페이지
        # project_pk 를 get 방식으로 보내어 해당 'pk' 를 가지고 있는 detail 페이지로 되돌아가기
        return reverse('projectapp:detail', kwargs={'pk' : self.request.GET.get('project_pk')})

    def get(self, request, *args, **kwargs):
        # 프로젝트와 유저정보를 취합하기 부분 추가 (get_object_or_404 라는 단축함수 사용하여 예외처리)
        # project_pk 를 가지고 있는 Project 를 찾는데,
        # 그게 만약 없다면(없는 프로젝트에 대한 구독의 경우) '페이지를 찾을 수 없음' 을 되돌려주도록
        project = get_object_or_404(Project, pk=self.request.GET.get('project_pk'))
        user = self.request.user   # user 찾기


        # user, project 가 각각 우리가 앞서 찾은 user, project 인 구독정보를 찾기
        subscription = Subscription.objects.filter(user=user,
                                                   project=project)
        if subscription.exists():   # 구독 정보가 존재한다면, 지우기
            subscription.delete()
        else: # 구독 정보가 존재하지 않는다면
            Subscription(user=user, project=project).save() # -> 앞서 찾은 user,project 로 구독정보를 만들어야함.
            # 대문자 S

        return super(SubscriptionView, self).get(request, *args, **kwargs)

@method_decorator(login_required, 'get') # 로그인 하였는지
class SubscriptionListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'subscribeapp/list.html'
    paginate_by = 5

    def get_queryset(self): # 가지고 오는 게시글들의 조건을 바꿀 수 있는 함수
        projects = Subscription.objects.filter(user=self.request.user).values_list("project") #values_list : 값들을 리스트화 시킨다는 의미.
        article_list = Article.objects.filter(project__in=projects) # 바로 위에서 find 한 projects
        return article_list