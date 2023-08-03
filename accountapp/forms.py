# pragmatic/accountapp/forms.py

from django.contrib.auth.forms import UserCreationForm

class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].disabled = True
        # 필드로 가지고 있는 값들 중에 username 을 disabled 라는 속성을 활성화
        # 만약 바로 위 self.fields 코드가 없다면
        # 우리가 import 한 UserCreationForm 과 그걸 상속받은 AccountUpdateForm은 똑겉은 form 이 됨
        # 이 한줄이 추가 됨 으로써 초기화 이후에 username 의 칸을 비활성화 시켜줌