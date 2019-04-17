from django.shortcuts import render
from django.http import HttpResponse
from .models import BookInfo

# Create your views here.
"""
视图函数
将函数和路由绑定
"""


def index(request):
    return HttpResponse('首页')


def list(request):
    return HttpResponse('列表页')


def detail(request,id):
    print(id)
    try:
        book = BookInfo.objects.get(pk=int(id))
        return HttpResponse(book)
    except:
        return HttpResponse('请输入正确id')
