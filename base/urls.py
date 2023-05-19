from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about_us/', views.aboutUs, name='aboutUs'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('projects/', views.projects, name='projects'),
    path('topics/', views.topics, name='topics'),

    path('add-topic/', login_required(views.addTopic), name='addTopic'),
    path('add-project/', login_required(views.addProject), name='addProject'),
]
