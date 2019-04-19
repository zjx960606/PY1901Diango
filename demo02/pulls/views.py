from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from .models import WenTi,TouPiao

# Create your views here.

def index(request):
    return render(request,'demo_pro/index.html',{'username':'zjx'})

def list1(request):
    wenti = WenTi.objects.all()
    return render(request,'demo_pro/list1.html', {'wenti':wenti})

def detail(request,id):
    tp = WenTi.objects.get(pk=id)

    return render(request,'demo_pro/detail.html',{'tp':tp})

def jishu(request,tpid):
    pid = request.POST['cont']
    print('----------', pid)
    t1=TouPiao.objects.get(pk=pid)
    t1.num +=1
    t1.save()

    # return render(request, 'demo_pro/detail.html',{'tp':tp})
    return HttpResponseRedirect('/index/list1/')