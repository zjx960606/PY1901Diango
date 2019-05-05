from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


# Create your models here.

# 用户表
class StuUser(User):
    stu_id = models.IntegerField(blank=True, null=True)
    college = models.CharField(max_length=20,blank=True,null=True)


# 图书表
class BookInfo(models.Model):
    # 书号
    isbn = models.IntegerField()
    # 书名
    title = models.CharField(max_length=20)
    # 作者
    author = models.CharField(max_length=20)
    # 出版社
    press = models.CharField(max_length=20)
    # 出版商
    publishers = models.CharField(max_length=20)
    # 出版时间
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title



# 借阅历史表
class Borrowing(models.Model):
    # 借阅时间
    bor_time = models.DateTimeField(auto_now_add=True)
    # 归还时间
    re_time = models.DateTimeField(blank=True,null=True)
    # 借阅人
    borrower = models.ForeignKey(StuUser,on_delete=models.CASCADE)
    # 借阅书籍
    borrow_book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)
    # 借阅状态
    borrow_status = models.BooleanField(default=False)


class HotPic(models.Model):
    name = models.CharField(max_length=20)
    pic = models.ImageField(upload_to='hotpic')
    index = models.SmallIntegerField()


class MessageInfo(models.Model):
    title = models.CharField(max_length=20)
    massage = HTMLField()
