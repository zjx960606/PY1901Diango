from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from .models import StuUser, Borrowing, BookInfo,HotPic,MessageInfo
import datetime
from django.core.mail import send_mail,send_mass_mail
from django.conf import settings
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


# Create your views here.

def index(request):
    username = request.session.get('username')
    hots = HotPic.objects.all()
    mess = MessageInfo.objects.all()
    return render(request, 'index.html', {'username': username,'hots':hots,'mess':mess})


# 用户注册
def register(request):
    return render(request, 'register.html')


def registerhand(request):
    if request.method == 'GET':
        return redirect(reverse('bookapp:register'))
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        college = request.POST.get('college')
        number = request.POST.get('number')
        email = request.POST.get('email')
        users = StuUser.objects.all()
        try:
            for i in users:
                if username == i.username:
                    error = '该用户名已被注册'
                    return render(request, 'register.html', {'error': error})
            else:
                users = StuUser()
                users.username = username
                users.password = password
                users.college = college
                users.email = email
                users.stu_id = number
                users.is_active = False
                users.save()
                uid = users.id
                # 序列化ID
                serutil = Serializer(settings.SECRET_KEY,300)
                resid = serutil.dumps({'userid':uid }).decode("utf-8")

                send_mail('点击激活账户', "<a href ='http://127.0.0.1:8020/bookapp/active/%s' ></a> "%(resid),settings.DEFAULT_FROM_EMAIL,[email] )
        except Exception as e:
            print(e)
        return redirect(reverse('bookapp:login'))


# 用户登录

def login(request):
    if request.method == 'GET':
        return render(request, 'reader_login.html')
    else:
        error = None
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:

            user = StuUser.objects.get(username=username).username
            pwd = StuUser.objects.get(password=password).password

            if password == pwd and username == user:
                request.session['sid'] = StuUser.objects.get(username=username).id

                return redirect(reverse('bookapp:reader'))
            else:
                error = '密码不正确'
        except Exception as e:
            print(e)
            error = '用户名不存在'
        return render(request, 'reader_login.html', {'error': error})


def reader(request):
    sid = request.session.get("sid")
    username = StuUser.objects.get(pk=sid).username
    return render(request, 'reader.html', {'username': username})


def user_delete(request):
    request.session.clear()
    return redirect(reverse('bookapp:index'))

def reader_info(request):
    id = request.session.get('sid')
    users = StuUser.objects.get(pk=id)
    return render(request, 'reader_info.html', {'user': users})


# 借阅历史
def reader_histroy(request):
    id = request.session.get('sid')
    users = StuUser.objects.get(pk=id)
    histroys = users.borrowing_set.all()
    print(histroys)
    return render(request, 'reader_histroy.html', {'histroys': histroys})


# 查询
def reader_query(request):
    if request.method == "POST":
        item = request.POST['item']
        query = request.POST['query']
        if item == 'name':
            b = BookInfo.objects.filter(title=query)
            print(b)
            return render(request, 'reader_query.html', {'book': b})
        else:
            p = BookInfo.objects.filter(author=query)
            print(p)
            return render(request, 'reader_query.html', {'book': p})
    else:
        return render(request, 'reader_query.html')


# 书籍详情

def reader_book(request, id):
    if request.method == 'GET':
        book = BookInfo.objects.get(pk=id)
        return render(request, 'reader_book.html', {'book': book})
    else:
        book = BookInfo.objects.get(pk=id)
        reader = book.borrowing_set.all()
        print(reader, '11111111111111111')
        now = datetime.datetime.now()
        date_time = datetime.timedelta(days=30)
        bw = Borrowing()
        bw.re_time = now + date_time
        bw.borrow_book =book
        bw.borrower = StuUser.objects.get(username=request.session.get('username'))
        bw.save()
        return render(request, 'reader_book.html', {'book': book, 'reader': bw})



def edit(request):
    if request.method == 'GET':
        return render(request,'reader_edit.html')
    elif request.method == 'POST':
        title = request.POST['title']
        massage = request.POST['massage']

        message = MessageInfo(title=title,massage = massage)
        message.save()
        return redirect(reverse('bookapp:index'))


def mail(request):
    send_mail('Django邮件','Django可以发送邮件,<a href =" http://127.0.0.1:8020/bookapp/active/ "></a>', settings.DEFAULT_FROM_EMAIL,['2426259881@qq.com'])
    # send_mass_mail((('Django邮件1','Django可以发送邮件', settings.DEFAULT_FROM_EMAIL,['2426259881@qq.com']),
    #                 ('Django邮件2', 'Django可以发送邮件', settings.DEFAULT_FROM_EMAIL, ['2426259881@qq.com']),
    #                 ('Django邮件3', 'Django可以发送邮件', settings.DEFAULT_FROM_EMAIL, ['2426259881@qq.com'])))
    return HttpResponse('发送成功')


# 激活账户
def active(request, idstr):
    dser = Serializer(settings.SECRET_KEY,300)
    try:
        obj = dser.loads(idstr)
        user = StuUser.objects.get(pk=obj['userid'])
        user.is_active = True
        user.save()
        return redirect(reverse('bookapp:login'))
    except:
        return HttpResponse("连接失效")





def upload(request):
    if request.method == 'GET':
        return render(request,'reader_upload.html')
    elif request.method == 'POST':
        name = request.POST['name']
        index = request.POST['index']
        pic = request.FILES['pic']

        hp = HotPic(name=name, pic=pic, index=index,)
        hp.save()
        return redirect(reverse('bookapp:index'))

# ajax
def ajax(request):
    return render(request, 'ajax.html')

def ajaxajax(request):
    if request.method == 'GET':
        return HttpResponse('GET请求成功')
    elif request.method == 'POST':
        return HttpResponse('POST请求成功')


def ajaxlogin(request):
    print('123')
    if request.method == 'GET':
        return render(request,'ajaxlogin.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = StuUser.objects.filter(username=username, password=password).first()
        if user is None:
            return HttpResponse("登录失败")
        else:
            return HttpResponse("登陆成功")

def checkuser(request):
    if request.method == 'POST':
        username = request.POST['username']
        user = StuUser.objects.filter(username=username).first()
        if user is None:
            return HttpResponse("success")
        else:
            return HttpResponse("success")