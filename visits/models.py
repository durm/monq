#-*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from collections import Counter

CLOSED_STATUS_CHOICES = (
    ('normal', 'Нормально'),
    ('trouble', 'Аварийно'),
)

class ConfirmedFields(models.Model):
    
    confirmed = models.BooleanField(verbose_name="Подтверждено", default=False)
    confirmed_at = models.DateTimeField(verbose_name="Подтверждено в", blank=True, null=True)
    
    def confirm(self):
        assert not self.confirmed, "Already confirmed"
        self.confirmed = True
        self.confirmed_at = datetime.now()
        
    class Meta:
        abstract = True
        
class ClosedFields(models.Model):
    
    closed = models.BooleanField(verbose_name="Закрыт", default=False)
    closed_at = models.DateTimeField(verbose_name="Закрыт в", blank=True, null=True)
    closed_status = models.CharField(verbose_name="Статус закрытия", max_length=7, choices=CLOSED_STATUS_CHOICES, blank=True, null=True)
    closed_desc = models.TextField(verbose_name="Описание закрытия", blank=True, null=True)
    
    def close(self, closed_status=CLOSED_STATUS_CHOICES[0][0], closed_desc=""):
        assert not self.closed, "Already closed"
        self.closed = True
        self.closed_at = datetime.now()
        self.closed_status = closed_status
        self.closed_desc = closed_desc
    
    class Meta:
        abstract = True
        
class OpenedFields(models.Model):
    
    opened_at = models.DateTimeField(verbose_name="Открыт в", auto_now_add=True, blank=False, null=False)
    
    class Meta:
        abstract = True
        
class ClientFields(models.Model):
    
    client = models.ForeignKey(User, related_name="+up+", verbose_name="Клиент", blank=False, null=False)
    client_comment = models.TextField(verbose_name="Комментарий клиента", blank=True, null=True)
    
    class Meta:
        abstract = True
    
class Position(models.Model):
    
    name = models.TextField(verbose_name="Наименование", blank=False, null=False)
    desc = models.TextField(verbose_name="Описание", blank=False, null=False)
    price = models.FloatField(verbose_name="Цена", blank=False, null=False)
    
class PositionPair(models.Model):
    
    position = models.ForeignKey(Position)
    current_price = models.FloatField()
        
    def set_current_price(self):
        self.current_price = self.position.price
        
class Check(OpenedFields):
    
    position_pairs = models.ManyToManyField(PositionPair, verbose_name="Позиции")
    
    def summary(self):
        c = Counter()
        c.update(self.position_pairs.all())
        return ((k[0], k[1], v, k[1]*v) for k,v in c)

class Visit(ClientFields, OpenedFields, ClosedFields, ConfirmedFields):
    
    checks = models.ManyToManyField(Check, verbose_name="Счета", null=True, blank=True)
    
    @staticmethod
    def get_opened_session(client):
        return Visit.objects.filter(client=client, closed=False).first()
    
    

