from django.shortcuts import render
from .models import Club
from django.apps import apps

def clubs(request):
    context = apps.get_model('main', 'Settings').get_settings()
    context["clubs"] = Club.objects.filter(is_visible=True)
    return render(request, 'clubs/clubs.html', context=context)


