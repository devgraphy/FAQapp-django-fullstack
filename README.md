

# 모델 설계

질문 답변 게시판이므로 질문과 답변에 해당하는 모델이 있어야 한다.

[Model field reference | Django documentation | Django (djangoproject.com)](https://docs.djangoproject.com/en/3.0/ref/models/fields/#field-types)

## 모델 속성 구상

질문 모델

| 속성명      | 설명               |
| ----------- | ------------------ |
| subject     | 질문의 제목        |
| content     | 질문의 내용        |
| create_date | 질문을 작성한 일시 |



답변 모델

| 속성명      | 설명                                                        |
| ----------- | ----------------------------------------------------------- |
| question    | 질문(어떤 질문의 답변이니 알아야 하므로 질문 속성이 필요함) |
| content     | 답변의 내용                                                 |
| create_date | 답변을 작성한 일시                                          |



## 데이터 생성, 저장, 조회

### 1. 장고 shell 실행

`python manage.py shell`

### 2. Question, Answer 모델 임포트

`from faqapp.models import Question, Answer`

### 3. Question 모델로 Qestion 모델 데이터 만들기

```python
from django.utils import timezone
q = Question(subject='faqapp이 뭔가요?', content='faqapp에 대해서 알고 싶습니다.', create_date=timezone.now())
q.save()
q.id	# id는 데이터의 유일한 값이며, pk라고 부르기도 한다. id값은 데이터를 생성할 때마다 1씩 증가한 값으로 자동으로 입력된다.
```

### 4. Question 모델 데이터 모두 조회

```python
>>>Question.objects.all()
<QuerySet [<Question: Question object (1)>, <Question: Question object (2)>]>
```

장고에서 저장된 모델 데이터는 Question.objects를 사용하여 조회 가능

Question.objects.all()은 Question에 저장된 모든 데이터를 조회하는 함수

현재 QuerySet 에는 2개의 Question 객체가 포함되어 있다.

1, 2는 장고에서 Question 모델 데이터에 자동으로 입력해 준 id이다.



### 5. Question 모델 데이터 조회 결과에 속성값 보이기

위의 결과는 데이터 유형을 출력한 것이므로 사람이 보기 불편하다. 이때 Question 모델에 `__str__` 메서드를 추가하면 된다.

모델이 수정되었으므로 장고 shell을 quit()명령으로 종료 후 다시 시작해서 조회한다.

```python
class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject
```

> 모델이 수정되었는데 왜 makemigrations, migrate 명령을 실행하지 않을까?
>
> makemigrations, migrate 명령은 모델의 속성이 추가되거나 변경된 경우에 실행하는 명령이다. 지금은 메서드가 추가된 것이므로 이 과정은 하지 않아도 된다.



### 6. 조건으로 Question 모델 데이터 조회

```python
>>> Question.objects.filter(id=1)
<QuerySet [<Question: pybo가 무엇인가요?>]>
```

### 7. Question 모델 데이터 하나만 조회

```python
>>>Question.objects.get(id=1)
<Question: pybo가 무엇인가요?>
```

### 8. get으로 조건에 맞지 않는 데이터 조회

오류 발생

### 9. filter로 조건에 맞지 않는 데이터 조회

빈 Queryset 반환

### 10. 제목의 일부를 이용하여 데이터 조회

`filter`, `__contains`



## 데이터 수정

```python
>>> q = Question.objects.get(id=2)
>>> q
<Question: 장고 모델 질문입니다.>
>>> q.subject = 'Django Model Question'
>>> q.save()
>>> q
<Question: Django Model Question>
```



## 데이터 삭제

```python
>>> q = Question.objects.get(id=1)
>>> q.delete()
(1, {'pybo.Question': 1})
>>> Question.objects.all()
<QuerySet [<Question: Django Model Question>]>
```

delete 함수를 수행하면 해당 데이터가 데이터베이스에서 즉시 삭제되며, 삭제된 데이터의 추가 정보가 반환된다. `(1, {'pybo.Question': 1})`에서 앞의 1은 삭제된 Question 모델 데이터의 id를 의미하고 `{'pybo.Question': 1}`은 삭제된 모델 데이터의 개수를 의미한다.

> Answer 모델을 만들 때 ForeignKey로 Question 모델과 연결한 것이 기억나는가? 만약 삭제한 Question 모델 데이터에 2개의 Answer 모델 데이터가 등록된 상태라면 `(1, {'pybo.Answer': 2, 'pybo.Question': 1})`와 같이 삭제된 답변 개수도 함께 반환될 것이다.



## 연결된 모델 데이터 조회

앞서 Answer 모델을 만들 때 ForeignKey로 Question 모델과 연결하였다. Answer 모델은 Question 모델과 연결되어 있으므로 데이터를 만들 때 Question 모델 데이터가 필요하다.



### 1. Answer 모델 데이터 만들기

```python
>>> q = Question.objects.get(id=2)
>>> q
<Question: Django Model Question>
>>> from django.utils import timezone
>>> a = Answer(question=q, content='네 자동으로 생성됩니다.', create_date=timezone.now())
>>> a.save()
>>> a.id
```

### 2. Answer 모델 데이터 조회

```python
>>> a = Answer.objects.get(id=1)
>>> a
<Answer: Answer object (1)>
```

### 3. 연결된 데이터로 조회: 답변에 있는 질문 조회

Answer 모델 데이터에는 Question 모델 데이터가 연결되어 있으므로 Answer 모델 데이터에 연결된 Question 모델 데이터를 조회할 수 있다.

```python
>>> a.question
<Question: Django Model Question>
```

### 4. 연결된 데이터로 조회: 질문을 통해 답변 찾기

`_set`을 사용하면 된다.

```python
>>> q.answer_set.all()
<QuerySet [<Answer: Answer object (1)>]>
```

>Question 모델과 Answer 모델처럼 서로 연결되어 있으면 연결모델명_set과 같은 방법으로 연결된 데이터를 조회할 수 있다. 그리고 아마 여러분은 연결모델명_set을 써야 하는 경우와 그렇지 않은 경우가 헷갈릴 것이다.
>
>이때는 질문과 답변이 달리는 게시판을 상식적으로 생각해 보자. 질문 1개에는 1개 이상의 답변이 달릴 수 있으므로 질문에 달린 답변은 q.answer_set으로 조회해야 한다(답변 세트를 조회). 답변은 질문 1개에 대한 것이므로 애초에 여러 개의 질문을 조회할 수 없다. 다시 말해 답변 1개 입장에서는 질문 1개만 연결되어 있으므로 a.question만 실행할 수 있다. 1개의 답변으로 여러 개의 질문을 a.question_set으로 조회하는 것은 불가능하며, 상식적으로 생각해 보아도 이상하다. 연결모델명_set은 정말 신통방통한 장고의 기능이 아닐 수 없다. 연결모델명_set은 자주 사용할 기능이니 꼭 기억하자.



## 장고 Admin에 데이터 검색 기능 추가

```python
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(Question, QuestionAdmin)
```

