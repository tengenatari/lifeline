from django.shortcuts import render
from .models import Player
import datetime
from django.apps import apps

def index_players(request):
    context = apps.get_model('main', 'Settings').get_settings()
    # context["players"] = Player.objects.filter(
    #                   last_game_date__range=[datetime.datetime.now() - datetime.timedelta(days=3*365),
    #                                          datetime.date.today()],
    #                                          is_visible=True).order_by('-rating')
    
    context["players"] = Player.objects.filter(is_visible=True).order_by('-rating')

    return render(request, 'players/players.html',
                  context=context)
