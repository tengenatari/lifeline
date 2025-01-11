from django.shortcuts import render
from news.models import Post
# Create your views here.


def index_news(request):
    return render(request, 'news/news.html', context={'posts': Post.objects.all()})
