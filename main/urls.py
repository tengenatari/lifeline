from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about),
    path("favicon.ico", views.favicon),
]