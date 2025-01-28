from django.shortcuts import render
from .models import Post



def index_news(request):
    return render(request, 'news/news.html', context={'posts': Post.objects.all()})
