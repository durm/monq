#-*- coding: utf-8 -*-

from django.contrib import admin
from visits.models import *

class VisitAdmin(admin.ModelAdmin):
    list_display = ['client', 'opened_at' , 'confirmed', 'confirmed_at', 'closed', 'closed_at', 'closed_status']
    
admin.site.register(Visit, VisitAdmin)

class CheckAdmin(admin.ModelAdmin):
    list_display = ['id', 'opened_at' , 'confirmed', 'confirmed_at', 'closed', 'closed_at', 'closed_status']
admin.site.register(Check, CheckAdmin)

class PositionPairAdmin(admin.ModelAdmin):
    pass
admin.site.register(PositionPair, PositionPairAdmin)

class PositionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Position, PositionAdmin)
