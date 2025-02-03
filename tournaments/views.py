from django.shortcuts import render
from .models import Tournament
from django.apps import apps


def index_tournaments(request):
    context = apps.get_model('main', 'Settings').get_settings()
    context["tournaments"] = Tournament.objects.filter(is_visible=True).order_by('-date')
    
    return render(request, 'tournaments/tournaments.html',
                  context=context)
