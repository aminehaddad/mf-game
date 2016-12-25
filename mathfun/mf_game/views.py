from django.shortcuts import render

def game(request, template="mf_game/game.html"):
    data = {}
    return render(request, template, data)
