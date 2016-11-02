# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from SentiMap import views
urlpatterns = [
  url(r'^map/(?P<MapName>(\w)+)/$', views.map, name='map'),#這樣做似乎是對應到首頁
  url(r'^relation/(?P<MapName>(\w)+)/$', views.relation, name='relation'),
]