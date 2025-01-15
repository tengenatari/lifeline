from django.shortcuts import render

def index_players(request):
    return render(request, 'players/players.html')