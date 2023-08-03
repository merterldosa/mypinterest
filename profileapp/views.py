# pragmatic/profileapp/views.py

from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorators import profile_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile
# Create your views here.

class ProfileCreateView(CreateView):
    model = Profile # 모델은 우리가 만든 Profile 사용
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm # 우리가 만든 ModelForm
    template_name = 'profileapp/create.html'

    # 추가한 부분
    def form_valid(self, form):
        temp_profile = form.save(commit=False)
        temp_profile.user = self.request.user
        temp_profile.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})

@method_decorator(profile_ownership_required, 'get') # 추가
@method_decorator(profile_ownership_required, 'post') # 추가
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:detail')
    template_name = 'profileapp/Update.html'

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})