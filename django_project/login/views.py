from django.shortcuts import render, reverse,redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import BookInfo, HeroInfo
from django.template import loader

# Create your views here.
"""
视图函数
将函数和路由绑定
"""


def index(request):
    print(request.session.get('username'))
    return render(request, 'tempdemo/index.html', {'username':request.session.get('username')})

def login1(request):
    if request.method == 'GET':
        return render(request,'tempdemo/login1.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        request.session['username'] = username
        request.session['password'] = password
        return redirect(reverse('login:index'))

def loginout(request):
    request.session.clear()
    return redirect('login:index')


def list(request):
    # return HttpResponse('列表页')
    book = BookInfo.objects.all()
    return render(request, 'tempdemo/list.html', {'book': book})


def detail(request, id):
    book = BookInfo.objects.get(pk=id)
    return render(request, 'tempdemo/detail.html', {"book": book})



def delete(request, id):
    try:
        BookInfo.objects.get(pk=id).delete()
        book = BookInfo.objects.all()
        return render(request, 'tempdemo/list.html', {'book': book})
    except:
        return HttpResponse('删除失败')


def addhero(request, bookid):
    # book = BookInfo.objects.get(pk=id)
    # HeroInfo.objects.get()
    return render(request, 'tempdemo/addhero.html', {'bookid': bookid})


def addherohand(request):
    bookid = request.POST['bookid']
    hname = request.POST['hname']
    hgender = request.POST['sex']
    hcontent = request.POST['hcontent']
    print(hname, hgender, hcontent, bookid)

    book = BookInfo.objects.get(pk=bookid)
    hero = HeroInfo()
    hero.hname = hname
    hero.hgender = True
    hero.hcontent = hcontent
    hero.hbook = book
    hero.save()
    return HttpResponseRedirect('/detail/' + str(bookid) + '/', {'book':book})


def deletehero(request, id):
    try:
        book_id = HeroInfo.objects.get(pk=id).hbook.id
        HeroInfo.objects.get(pk=id).delete()

        return HttpResponseRedirect('/detail/' + str(book_id) + '/')
    except:
        return HttpResponse('删除失败')


def addbook(request):
    return render(request, 'tempdemo/addbook.html')


def addbookhand(request):
    bname = request.POST['bname']
    btitle = request.POST['btitle']
    book = BookInfo()
    book.bname = bname
    book.btitle = btitle
    book.save()
    return HttpResponseRedirect('/list/')


def gaibook(request, gid):
    return render(request, 'tempdemo/gaibook.html', {'sid': gid})


def gaibookhand(request):
    id = request.POST['bid']
    bname = request.POST['bname']
    btitle = request.POST['btitle']
    book = BookInfo.objects.get(pk=id)
    book.bname = bname
    book.btitle = btitle
    book.save()
    return HttpResponseRedirect('/list/')


def gaihero(request, gid):
    return render(request, 'tempdemo/gaihero.html', {'kid': gid})


def gaiherohand(request):
    kid = request.POST['kid']

    hname = request.POST['hname']
    # hgender = request.POST['sex']
    hcontent = request.POST['hcontent']

    # bk = BookInfo.objects.get(pk=kid)
    hero = HeroInfo.objects.get(pk=kid)
    hero.hname = hname
    hero.hgender = True
    hero.hcontent = hcontent
    # hero.hbook = bk
    hero.save()
    return HttpResponseRedirect('/detail/' + str(kid) + '/')
