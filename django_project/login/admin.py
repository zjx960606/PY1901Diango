from django.contrib import admin
from .models import BookInfo, HeroInfo


# Register your models here.


# 关联注册
class HeroInfoInline(admin.StackedInline):
    model = HeroInfo
    extra = 1

# 自定义管理页面
class BookInfoAdmin(admin.ModelAdmin):
    # 显示字段，可以点击列头进行排序
    list_display = ['bname', 'btitle']
    # 过滤字段，过滤框会出现在右侧
    list_filter = ['bname', 'btitle']
    # 搜索字段，搜索框会出现在上侧
    search_fields = ['bname']
    list_per_page = 2
    inlines = [HeroInfoInline]


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['skill', 'hgender', 'hcontent']
    list_filter = ['hname', 'hgender']
    search_fields = ['hname', 'hcontent']
    list_per_page = 2






# 注册模型
admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)

"""
后台，可以用少量的代码就拥有一个强大的后台
"""
