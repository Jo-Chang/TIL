from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
"""
# Article 클래스의 인스턴스 생성
article = Article()

# article 인스턴스에 title과 content 인스턴스 변수에 값을 저장
article.title = '제목'
article.content = '내용'

# 테이블에 레코드 하나 생성을 위해 저장 (인스턴스 메서드 save 호출)
article.save()


article = Article(title='title', content='django!!')
article.save()


Article.objects.create(title='third', content='django!!!')
"""