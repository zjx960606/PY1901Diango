from django.contrib import admin
from .models import StuUser, BookInfo, Borrowing,HotPic,MessageInfo

# Register your models here.

admin.site.register(StuUser)
admin.site.register(BookInfo)
admin.site.register(Borrowing)
admin.site.register(HotPic)
admin.site.register(MessageInfo)
