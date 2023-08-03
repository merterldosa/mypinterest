from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from accountapp.models import HelloWorld
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.models import User
from accountapp.forms import AccountUpdateForm

def hello_world(request):
    # 로그인이 되어있다면 정상적으로 작동
    if request.user.is_authenticated:
        if request.method == 'POST':

            get = request.POST.get('hello_world')
            new_hello_world = HelloWorld()
            new_hello_world.text = get
            new_hello_world.save()

            return HttpResponseRedirect(reverse('accountapp:hello_world'))
        else:

            hello_world_list = HelloWorld.objects.all()
            return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})

    # 아닌 경우, 로그인하는 창으로 되돌려 보내기
    else:
        return HttpResponseRedirect(reverse('accountapp:login'))

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'  # 추가
    template_name = 'accountapp/detail.html'

class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm #UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().get(*args, **kwargs)  # 기존의 방식대로 하고
        else:
            return HttpResponseForbidden()

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().get(*args, **kwargs)  # 기존의 방식대로 하고
        else:
            return HttpResponseForbidden()

class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().get(*args, **kwargs)  # 기존의 방식대로 하고
        else:
            return HttpResponseForbidden()

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().get(*args, **kwargs)  # 기존의 방식대로 하고
        else:
            return HttpResponseForbidden()
