from django.urls import path
from . import views

app_name = 'clicker'

urlpatterns = [
    path('', views.home, name='home'),
    path('click/', views.click_plant, name='clicker_page'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('rewards/', views.rewards, name='rewards'),
    path('register/', views.register, name='register'),
]
