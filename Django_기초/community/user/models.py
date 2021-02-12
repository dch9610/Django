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


    class Meta:
        # 테이블명 지정
        db_table = 'Online_user'
                    
                    