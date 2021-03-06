from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
   
    # custom view 
    url(r'^recommend_games/', views.recommend_games, name='recommend_games'),
    url(r'^onLoadGameData/', views.onLoadGameData, name='onLoadGameData')

]