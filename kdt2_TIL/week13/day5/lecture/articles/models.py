from django.db import models

# Create your models here.

class Article(models.Model):
    # 필드 이름 / 데이터 타입(모델 필드 클래스) / 제약조건(모델 필드 클래스의 키워드 인자)
    # id는 장고가 자동 생성
    title = models.CharField(max_length=10)  # 길이 제한을 줘야함
    content = models.TextField()    # 길이에 제한 없음
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    