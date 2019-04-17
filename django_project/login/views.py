from django.shortcuts import render
from django.http import HttpResponse
from .models import BookInfo
from django.template import loader

# Create your views here.
"""
视图函数
将函数和路由绑定
"""


def index(request):

    # index1= loader.get_template('tempdemo/index.html')
    #
    # cont = {'username':'zjx'}
    # # 使用变量参数渲染模板
    # result = index1.render(cont)
    # # 返回模板
    # return HttpResponse(result)
    return render(request, 'tempdemo/index.html', {'username': 'zjx'})



def list(request):
    # return HttpResponse('列表页')
    book = BookInfo.objects.all()
    return render(request, 'tempdemo/list.html', {'book':book})


def detail(request,id):
    # print(id)
#     # try:
#     #     book = BookInfo.objects.get(pk=int(id))
#     #     return HttpResponse(book)
#     # except:
#     #     return HttpResponse('请输入正确id')
    book = BookInfo.objects.get(pk=id)
    return render(request, 'tempdemo/detail.html', {"book":book})