# pragmatic/profileapp/forms.py

from django.forms import ModelForm
from profileapp.models import Profile

class ProfileCreationForm(ModelForm): #ModelForm 상속 받기
    class Meta:
        model = Profile
        fields = ['image','nickname','message'] # 사용할 필드
        # model 에서는 user 라는 필드가 하나 더 있긴 하지만
        # user 는 서버에서 따로 처리를 할것