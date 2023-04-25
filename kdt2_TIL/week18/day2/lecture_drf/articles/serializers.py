from rest_framework import serializers
from .models import Article, Comment

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content', )
        
                
class ArticleSerializer(serializers.ModelSerializer):
    
    class MyCommentSerializer(serializers.ModelSerializer):
      class Meta:
        model = Comment
        fields = ('id', 'content',)
        
    # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)   # PK만 참조 가능한 문제
    comment_set = MyCommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count')
    
    class Meta:
        model = Article
        fields = '__all__'
        
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        # fields = ('id', 'content',)
        # 유효성 검사에서는 제외시키고, 데이터 조회시에는 제공하는 데이터
        # 읽기 전용 속성
        read_only_fields = ('article',)