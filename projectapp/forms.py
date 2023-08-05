from django.forms import ModelForm

from projectapp.models import Project

class ProjectCreationForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'image'] # ModelForm 을 기반으로 3가지를 입력으로 받는다