# pragmatic/profileapp/views.py

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile
# Create your views here.

class ProfileCreateView(CreateView):
    model = Profile # 모델은 우리가 만든 Profile 사용
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm # 우리가 만든 ModelForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/create.html'

    # 추가한 부분
    def form_valid(self, form):
        temp_profile = form.save(commit=False)
        temp_profile.user = self.request.user
        temp_profile.save()
        return super().form_valid(form)