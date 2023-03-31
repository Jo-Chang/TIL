from django.shortcuts import redirect


def index(_):
    # return redirect('accountbooks:index')   # urls 경로 지정 수 수정
    return redirect('account-books/')