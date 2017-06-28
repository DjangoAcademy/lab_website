from django.conf.urls import *
from . import views

urlpatterns = [url(r'^$', views.HomePage, name='HomePage'),
               url(r'^_nav', views._nav, name='BaseOld'),
               url(r'^Base', views.BasePage, name='BasePage'),
               url(r'^Head', views.Header, name='BasePage'),
               url(r'^adams', views.Adams, name='AdamsPage'),
               url(r'^home', views.Home, name='newHome'),
               url(r'^test', views.Garage, name='GarTest'),
]
