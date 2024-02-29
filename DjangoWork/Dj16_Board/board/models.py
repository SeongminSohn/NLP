from django.db import models
from django.db.models.functions import Now

# Create your models here.

class Post(models.Model):
    subject = models.CharField(max_length=200) # 글제목, 필수(NN)
    user = models.CharField(max_length=20) # 작성자, 필수(NN)
    content = models.TextField(null=True) # 글내용, null 허용
    view_cnt = models.IntegerField(default=0) # 조회수, 기본값 0
    reg_date = models.DateTimeField(default=Now()) # 작성일시, 기본값 현재시간

