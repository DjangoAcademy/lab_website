from django.conf.urls import *
from . import views

urlpatterns = [url(r'^$', views.HomePage, name='HomePage'),
               url(r'^Base', views.BasePage, name='BasePage'),
               url(r'^ODU', views.ODUHead, name='BasePage'),
]
