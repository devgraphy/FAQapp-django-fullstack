

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

