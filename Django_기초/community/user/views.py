from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.hashers import make_password # 비밀번호 암호화
from .models import user

# Create your views here.
def register(request):
    if request.method == "GET":
        return render(request, 'register.html')

    elif request.method == "POST":
        # name 값 받기
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        re_password = request.POST.get('re_password', None)


        res_data = {}

        # 값이 다 들어가지 않은 경우
        if not (username and password and re_password):
            res_data['error'] = "모든 값을 입력해야합니다."

        # 비밀번호가 다를경우
        if password != re_password:
            res_data['error'] =  '비밀번호가 다릅니다.'
        
        else:
            # models에 user 클래스를 불러와 적용
            Cuser = user(
                username = username,
                password = make_password(password) # 비밀번호를 암호화
            )

            Cuser.save()

        return render(request, 'register.html', res_data)