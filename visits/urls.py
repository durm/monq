#-*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^start/$', 'visits.views.start', name='start_visit'),
    url(r'^current/$', 'visits.views.current', name='go_to_current_visit'),
    url(r'^visit/(?P<id>[0-9]+)/$', 'visits.views.go_to_visit', name='go_to_visit'),
    #(?P<num>[0-9]+)
    url(r'^close/$', 'visits.views.close', name='close_visit'),
    url(r'^check/start/$', 'visits.views.start_check', name='start_check'),
    url(r'^check/(?P<id>[0-9]+)/$', 'visits.views.go_to_check', name='go_to_check'),
    url(r'^add_position_form/$', 'visits.views.add_position_form', name='add_position_form'),
    url(r'^add_position/$', 'visits.views.add_position', name='add_position'),
)
