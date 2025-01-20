from django.conf import settings
from django.shortcuts import render
from .models import Player

def index_players(request):
    return render(request, 'players/players.html', context={'players': Player.objects.order_by('-rating')})