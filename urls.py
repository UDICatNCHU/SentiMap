# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
import SentiMap
urlpatterns = patterns('SentiMap.views',
  url(r'^map/$','map', name='map'),#這樣做似乎是對應到首頁
)
