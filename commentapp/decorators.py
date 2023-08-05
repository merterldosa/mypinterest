# /pragmatic/commentapp/decorators.py
from django.http import HttpResponseForbidden

from commentapp.models import Comment


def comment_ownership_required(func): # decorator 정의 (이 계정의 소유권이 필요하다는 이름)
    def decorated(request, *args, **kwargs): # request 를 받아
        # 우리가 원하는 작업 - 본인인지 확인하는 작업
        # get, post 등의 요청을 받으면서 pk 로 받은 값을 가지고 있는 User 객체가 user 가 되는 것
        comment = Comment.objects.get(pk=kwargs['pk'])
        # pk 를 확인해서 해당 pk 의 Comment 객체가 실제로 request 를 보낸 comment 과 같은지 아닌지 확인
        if not comment.writer == request.user: # 댓글의 저자가 지금 요청을 보내는 user 와 다르다면
            return HttpResponseForbidden()   # 금지 되었다고 내보내기
        return func(request, *args, **kwargs) # 같다면 그냥 보내주기
    return decorated
    # article_ownership_required 라는 decorator 를 만들었으니까 views.py 에 적용하기