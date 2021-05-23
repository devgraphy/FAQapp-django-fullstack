from django.contrib import admin
from .models import Question, Answer
# Register your models here.

# 장고 Admin에 데이터 검색 기능 추가
class QuestionAdmin(admin.ModelAdmin):
    search_fields=['subject']
admin.site.register(Question, QuestionAdmin)

class AnswerAdmin(admin.ModelAdmin):
    search_fields=['content']
admin.site.register(Answer,AnswerAdmin)