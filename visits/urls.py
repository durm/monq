#-*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^start/$', 'visits.views.start', name='start_visit'),
    url(r'^current/$', 'visits.views.current', name='go_to_current_visit'),
    url(r'^close/$', 'visits.views.close', name='close_visit'),
)
