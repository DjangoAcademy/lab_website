from django.conf.urls import *
from . import views

urlpatterns = [url(r'^', views.Teaching, name='Teaching'),
]
