#from django.conf.urls import url
from django.urls import re_path

from . import views

app_name = 'bill'

urlpatterns = [
    re_path(r'^$',views.index,name='index'),
    re_path(r'^bill/',views.cal_amount,name='cal_amount'),
]
