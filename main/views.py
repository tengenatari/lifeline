from django.shortcuts import render
from django.conf import settings
from django.http import FileResponse, HttpRequest, HttpResponse
from django.views.decorators.cache import cache_control
from django.views.decorators.http import require_GET

def index(request):
    return news(request)

def players(request):
    return render(request, 'players.html')
def tournaments(request):
    return render(request, 'tournaments.html')
def news(request):
    return render(request, 'news.html')
def clubs(request):
    return render(request, 'clubs.html')
def about(request):
    return render(request, 'about.html')

@require_GET
@cache_control(max_age=60 * 60 * 24, immutable=True, public=True)  # one day
def favicon(request: HttpRequest) -> HttpResponse:
    file = (settings.BASE_DIR / "static" / "images" / "favicon.png").open("rb")
    return FileResponse(file)

