from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def landing(request):
    return HttpResponseRedirect(reverse("game"))

def game(request, template="mf_game/game.html"):
    data = {}
    return render(request, template, data)
