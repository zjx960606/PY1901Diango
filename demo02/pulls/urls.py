from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^list1/$',views.list1),
    url(r'^detail/(\d+)/$', views.detail),
    url(r'^jishu/(\d+)/$', views.jishu)

]