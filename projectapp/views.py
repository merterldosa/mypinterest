from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.list import MultipleObjectMixin

from articleapp.models import Article
from projectapp.forms import ProjectCreationForm
from projectapp.models import Project


# Create your views here.
from subscribeapp.models import Subscription


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = 'projectapp/create.html'

    def get_success_url(self):
        return reverse('projectapp:detail', kwargs={'pk': self.object.pk})

class ProjectDetailView(DetailView, MultipleObjectMixin):
    model = Project
    context_object_name = 'target_project'
    template_name = 'projectapp/detail.html'
    paginate_by = 25

    def get_context_data(self, **kwargs):
        project = self.object   # object : 현재 project 페이지
        user = self.request.user

        # 유저가 로그인을 했는지 안했는지 확인
        if user.is_authenticated: # 유저가 접속이 되있다면, usr 와 project 가 각각 user, project 인 구독정보를 찾고
            subscription = Subscription.objects.filter(user=user, project=project)
        # 유저가 접속되어있지 않는다면 구독 버튼 자체가 없기 떄문에 else 구문은 생략
        else:
            subscription = None

        object_list = Article.objects.filter(project=self.get_object())
        # 최종적으로 템플릿으로 넘어갈때는 context_data 안에다가 구독 정보를 우리가 찾은 'subsriptiom' 으로 대체
        # 이런식으로 구독 정보가 있는지 없는지 확인
        return super(ProjectDetailView, self).get_context_data(object_list=object_list,
                                                               subscription=subscription,
                                                               **kwargs)
class ProjectListView(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'projectapp/list.html'
    paginate_by = 5