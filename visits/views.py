#-*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response, redirect
from visits.models import *
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

def landing(request):
    return render_to_response("landing.html")

@login_required
def start(request):
    
    current_visit = Visit.get_opened_session(request.user)
    if current_visit is not None :
        return redirect(reverse("go_to_current_visit"))

    visit = Visit.objects.create(client=request.user)
    visit.save()    
    
    return redirect(reverse("go_to_current_visit"))

@login_required    
def current(request):
    
    current_visit = Visit.get_opened_session(request.user)
    if current_visit is None :
        return redirect(reverse("landing"))
    
    return render_to_response("current_visit.html", {"visit":current_visit})

@login_required    
def close(request):
    
    current_visit = Visit.get_opened_session(request.user)
    if current_visit is None :
        return redirect(reverse("landing"))
    
    current_visit.close()
    current_visit.save()
    
    return render_to_response("visit.html", {"visit":current_visit})
