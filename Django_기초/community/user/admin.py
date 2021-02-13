from django.contrib import admin
from .models import user

# Register your models here.

# user 추가하기
class userAdmin(admin.ModelAdmin):
    # 값을 웹 상에 보여주기
    list_display = ('username', 'password')

admin.site.register(user, userAdmin)
