from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
from django.shortcuts import get_object_or_404, get_list_or_404


# Create your views here.

# 4. 해당 VIEW 함수가 어떤 HTTP 요청 메서드를 허용하는지 결정하는 데코레이터 작성
# DRF VIEW 함수에서 필수
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
    # 1. 제공할 게시글 목록 조회
        # articles = Article.objects.all()
        articles = get_list_or_404(Article)
        
        # 2. 게시글 목록 데이터를 직렬화(serialization)
        serializer = ArticleListSerializer(instance=articles, many=True) # 다중 데이터(목록) 옵션 many
        
        # 3. 직렬화된 데이터를 json 데이터로 응답
        return Response(serializer.data)

    elif request.method == 'POST':
        # 사용자 데이터를 받아서 serializer로 직렬화
        serializer = ArticleSerializer(data=request.data)
        # 유효성 검사
        if serializer.is_valid(raise_exception=True):
        # if serializer.is_valid():
            serializer.save()
            # 생성 성공 시 201 응답
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # 생성 실패 시 400 응답
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk: int):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    
    if request.method == 'GET':
        serializer = ArticleSerializer(instance=article)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = ArticleSerializer(instance=article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET'])
def comment_list(request):
    # comments = Comment.objects.all()
    comments = get_list_or_404(Comment)
    
    serializer = CommentSerializer(instance=comments, many=True)
    return Response(data=serializer.data)
    
    
@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    # comment = Comment.objects.get(pk=comment_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    
    if request.method == 'GET':
        serializer = CommentSerializer(instance=comment)
        return Response(data=serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(instance=comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data)


@api_view(['POST'])
def comment_create(request, article_pk: int):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        comment = serializer.save(article=article)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)