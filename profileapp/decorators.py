#profileapp/decorators.py
from django.http import HttpResponseForbidden
from profileapp.models import Profile

def profile_ownership_required(func): # decorator 정의 (이 계정의 소유권이 필요하다는 이름)
    def decorated(request, *args, **kwargs): # request 를 받아
        # 우리가 원하는 작업 - 본인인지 확인하는 작업
        # get, post 등의 요청을 받으면서 pk 로 받은 값을 가지고 있는 Profile 객체가 profile 가 되는 것
        # urls 에서 update<int:pk> 로 받는 이 pk 로 이 profile 의 주인을 학인하고
        profile = Profile.objects.get(pk=kwargs['pk'])
        # pk 를 확인해서 이 profile 의 유저가 요청 보낸 유저와 같지 않다면
        if not profile.user == request.user:
            return HttpResponseForbidden() # 페이지를 표시할 수 없음을 내보내기
        return func(request, *args, **kwargs) # 아닌 경우는 그대로 보내주기
    return decorated
    # proflle_ownership_required 라는 decorator 를 만들었으니까 이를 views.py 에 적용하기