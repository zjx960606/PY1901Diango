from django.conf.urls import url
from . import views
app_name = 'bookapp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^registerhand/$', views.registerhand, name='registerhand'),
    url(r'^login/$', views.login, name='login'),
    url(r'^reader/$',views.reader,name='reader'),
    url(r'^reader_info/$',views.reader_info, name='reader_info'),
    url(r'^reader_histroy/$', views.reader_histroy, name='reader_histroy'),
    url(r'^reader_query/$', views.reader_query, name='reader_query'),
    url(r'^reader_book/(\d+)/$', views.reader_book, name='reader_book'),
    url(r'^user_delete/$', views.user_delete, name='user_delete'),
    url(r'^edit/$', views.edit,name='edit'),
    url(r'^upload/$',views.upload, name='upload'),

    # 发邮件
    url(r'^mail/$', views.mail, name='mail'),

    url(r'^active/(.*?)/$',views.active,name='active'),

    # ajax
    url(r'^ajax/$', views.ajax, name='ajax'),
    url(r'^ajaxajax/$', views.ajaxajax,name='ajaxajax'),

    url(r'^ajaxlogin/$', views.ajaxlogin, name='ajaxlogin'),
    url(r'^checkuser/$', views.checkuser, name='checkuser'),
]