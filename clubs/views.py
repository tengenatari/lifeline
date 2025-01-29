from django.shortcuts import render
from . import models
from .models import Club


def clubs(request):

    return render(request, 'clubs/clubs.html',
                    context={'clubs': Club.objects.filter(is_visible=True)}
                    )


