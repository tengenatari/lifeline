from django.shortcuts import render, redirect
from django.conf import settings
from django.http import FileResponse, HttpRequest, HttpResponse
from django.views.decorators.cache import cache_control
from django.views.decorators.http import require_GET
from django.apps import apps


def index(request):
    return redirect("/players")


def about(request):
    context = apps.get_model('main', 'Settings').get_settings()
    return render(request, 'about.html', context=context)


@require_GET
@cache_control(max_age=60 * 60 * 24, immutable=True, public=True)  # one day
def favicon(request: HttpRequest) -> FileResponse:
    file = (settings.BASE_DIR / "static" / "images" / "favicon.png").open("rb")
    return FileResponse(file)
