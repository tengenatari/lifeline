from django.conf import settings
from django.shortcuts import render
from .models import Tournament
import datetime


def index_tournaments(request):
    return render(request, 'tournaments/tournaments.html',
                  context={'tournaments': Tournament.objects.order_by('-date')
                           }
                  )
