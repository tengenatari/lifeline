from django.conf import settings
from django.shortcuts import render
from .models import Player
import datetime
def index_players(request):
    return render(request, 'players/players.html',
                  context={'players': Player.objects.filter(
                      last_game_date__range=[datetime.datetime.now() - datetime.timedelta(days=3*365),
                                             datetime.date.today()]).order_by('-rating')
                           }
                  )