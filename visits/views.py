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

@login_required
def go_to_visit(request, id):
    visit = Visit.objects.get(id=id)
    return render_to_response("visit.html", {"visit":visit})

@login_required
def start_check(request):

    current_visit = Visit.get_opened_session(request.user)
    if current_visit is None :
        return redirect(reverse("landing"))

    check = Check.objects.create()
    check.save()
    current_visit.checks.add(check)

    return redirect(reverse("go_to_check", args=[check.id]))

@login_required
def go_to_check(request,id):

    current_visit = Visit.get_opened_session(request.user)
    if current_visit is None :
        return redirect(reverse("landing"))

    check = current_visit.checks.filter(id=id).first()

    assert check is not None, "Check is not in session"

    return render_to_response("current_check.html", {"check":check, "visit":current_visit})

@login_required
def add_position_form(request):
    
    current_visit = Visit.get_opened_session(request.user)
    if current_visit is None :
        return redirect(reverse("landing"))

    positions = Position.objects.all()
    return render_to_response("add_position_form.html", {"positions": positions, "visit": current_visit})
    
@login_required
def add_position(request):
    
    current_visit = Visit.get_opened_session(request.user)
    if current_visit is None :
        return redirect(reverse("landing"))

    check_id = request.POST.getlist("check")
    check = current_visit.checks.filter(id=check_id).first()

    assert check is not None, "Check is not in session"
    
    position_ids = request.POST.getlist("position")
    
    for position in Position.objects.filter(id__in=position_ids) :
        position_pair = PositionPair.objects.create(position=position, current_price=position.price)
        position_pair.save()
        check.position_pairs.add(position_pair)
        
    return redirect(reverse("go_to_check", args=[check_id]))
        
    
