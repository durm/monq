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
    
    return redirect(reverse("go_to_visit", args=[current_visit.id]))

def go_to_visit(request, id):
    visit = Visit.objects.get(id=id)
    return render_to_response("visit.html", {"visit":visit})

def start_check(request):

    current_visit = Visit.get_opened_session(request.user)
    if current_visit is None :
        return redirect(reverse("landing"))

    check = Check.objects.create()
    check.save()
    current_visit.checks.add(check)

    return redirect(reverse("go_to_check", args=[check.id]))

def go_to_check(request,id):

    current_visit = Visit.get_opened_session(request.user)
    if current_visit is None :
        return redirect(reverse("landing"))

    check = Check.objects.get(id=id)

    assert current_visit.checks.filter(id=check.id).first() is not None, "Check is not in session"

    return render_to_response("current_check.html", {"check":check})