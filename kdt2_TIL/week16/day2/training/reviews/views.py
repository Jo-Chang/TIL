from django.shortcuts import render, redirect
from .models import Review, Comment
from .forms import ReviewForm, CommentForm

# Create your views here.
def index(request):
    reviews = Review.objects.all()
    
    context = {
        'reviews': reviews,    
    }
    return render(request, 'reviews/index.html', context)


def redirect_index(_):
    return redirect('reviews:index')


def create(request):
    if request.method == 'GET':
        review_form = ReviewForm()
    else:
        review_form = ReviewForm(data=request.POST, files=request.FILES)
        if review_form.is_valid():
            review = review_form.save()
            return redirect('reviews:detail', review.pk)
    
    context = {
        'review_form': review_form,
    }
    return render(request, 'reviews/create.html', context)


def detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    comment_form = CommentForm()
    comments = review.comment_set.all()
    context = {
        'review': review,    
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'reviews/detail.html', context)


def delete(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    review.delete()
    return redirect_index(request)


def update(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.method == 'GET':
        review_form = ReviewForm(instance=review)
    else:
        review_form = ReviewForm(data=request.POST, files=request.FILES, instance=review)
        if review_form.is_valid():
            review = review_form.save()
            return redirect('reviews:detail', review.pk)
    
    context = {
        'review_form': review_form,
        'review': review,
    }
    return render(request, 'reviews/update.html', context)


def comments_create(request, review_pk):
    comment_form = CommentForm(data=request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.review = Review.objects.get(pk=review_pk)
        comment_form.save()

    return redirect('reviews:detail', review_pk)


def comments_delete(reuqest, review_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('reviews:detail', review_pk)