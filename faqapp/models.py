from typing import ContextManager
from django.db import models

# Create your models here.
class Question(models.Model):
    subject = models.CharField(max_length=200)  # 최대 200자까지 입력
    content = models.TextField()                # 글자 수 제한이 없는 데이터
    create_date = models.DateTimeField()      # 날짜, 시간 관련 속성

class Answer(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
"""
Answer 모델은 어떤 질문에 대한 답변이므로 Question 모델을 속성으로 가져야 한다. 이처럼 어떤 모델이 다른 모델을 속성으로 가지면 ForeignKey를 이용한다.
on_delete=models.CASCADE는 답변에 연결된 질문이 삭제되면 답변도 함께 삭제한다는 의미이다.
"""