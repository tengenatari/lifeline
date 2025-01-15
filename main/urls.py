from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tournaments', views.tournaments),
    path('clubs', views.clubs),
    path('about', views.about),
    path("favicon.ico", views.favicon),
]