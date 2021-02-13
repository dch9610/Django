# -*- coding:UTF-8 -*-
from django.db import models

# Create your models here.
class user(models.Model):
    username = models.CharField(max_length = 32,
                                verbose_name='사용자명')

    password = models.CharField(max_length = 64,
                                verbose_name='비밀번호')

    # dttm 데이터타입의 약자
    registerd_dttm = models.DateTimeField(auto_now_add = True,
                                        verbose_name='등록시간')

    # 문자열 변환 함수 (아이디로 나오게함)
    def __str__(self):
        return self.username


    class Meta:
        # 테이블명 지정
        db_table = 'Online_user'

        # 왼쪽 상단 Myaction 부분이 바뀜
        verbose_name = '유저 사용자'

        # 장고는 모델을 보여줄때 복수형으로 보여줌 (변경)
        verbose_name_plural = '유저 사용자'
                    
                    