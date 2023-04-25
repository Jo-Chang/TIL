from rest_framework import serializers
from .models import Article, Comment

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title',)
        
        
class ArticleSerializer(serializers.ModelSerializer):
    class CommentsInArticleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ('id','content','created_at','updated_at')
            
    comments = CommentsInArticleSerializer(many=True, read_only=True)
    comments_count = serializers.IntegerField(source='comments.count', read_only=True)
    
    class Meta:
        model = Article
        fields = '__all__'
        
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)