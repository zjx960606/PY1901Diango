# from django.contrib import admin
# from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'login'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list/$', views.list, name='list'),
    url(r'^detail/(\d+)/$', views.detail, name='detail'),
    url(r'^delete/(\d+)/$', views.delete, name='delete'),

    url(r'^addhero/(\d+)/$', views.addhero, name='addhero'),
    url(r'^/addherohand/$', views.addherohand, name='addherohand'),

    url(r'^deletehero/(\d+)/$', views.deletehero, name='deletehero'),

    url(r'addbook/$', views.addbook,name='addbook'),
    url(r'addbookhand/$', views.addbookhand,name='addbookhand'),

    url(r'gaibook/(\d+)/$',views.gaibook,name='gaibook'),
    url(r'gaibookhand/$',views.gaibookhand,name='gaibookhand'),

    url(r'gaihero/(\d+)/$', views.gaihero, name='gaihero'),
    url(r'gaiherohand/$',views.gaiherohand, name='gaiherohand'),

    url(r'login1/$', views.login1, name='login1'),
    url(r'loginout/$', views.loginout, name='loginout'),
]