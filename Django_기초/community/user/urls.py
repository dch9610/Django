from django.urls import path
from . import views

urlpatterns = [
    # 함수명을 적음
    path('register/', views.register)
]