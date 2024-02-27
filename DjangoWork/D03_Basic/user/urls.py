from django.urls import path
from user import views

urlpatterns = [

    path('list/', views.list),  # user/list/ => views.py 의 list 함수가 처리

]