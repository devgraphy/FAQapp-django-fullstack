from typing import ContextManager
from django.db import models

# Create your models here.
class Question(models.Model):
    subject = models.CharField(max_length=200)  # 최대 200자까지 입력
    content = models.TextField()                # 글자 수 제한이 없는 데이터
    create_date = models.DataTimeField()        # 날짜, 시간 관련 속성

