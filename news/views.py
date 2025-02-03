from django.shortcuts import render
from .models import Post
from django.apps import apps


def index_news(request):
    context = apps.get_model('main', 'Settings').get_settings()
    context["posts"] = Post.objects.all()
    return render(request, 'news/news.html', context=context)
