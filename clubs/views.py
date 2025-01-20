from django.shortcuts import render
from . import models
# Create your views here.


def clubs(request):

    return render(request, 'clubs/clubs.html')

