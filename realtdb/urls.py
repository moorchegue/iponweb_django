#-*- coding:utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('realtdb.views',
    url('^houses/$', 'house_list', name="realtdb-houses"),
    url('^apartments/$', 'apartment_list', name="realtdb-apartments"),
)
