from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about_us/', views.aboutUs, name='aboutUs'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),

    path('topics/', views.topics, name='topics'),
    path('add-topic/', login_required(views.create_topic), name='addTopic'),
    path('topic/delete/<int:pk>', login_required(views.TopicDelete.as_view()), name='deleteTopic'),
    path('topic/edit/<int:id>', login_required(views.edit_topic), name='editTopic'),

    path('projects/', views.projects, name='projects'),
    path('add-project/', login_required(views.create_project), name='addProject'),
    path('project/delete/<int:pk>', login_required(views.ProjectDelete.as_view()), name='deleteProject'),
    path('project/edit/<int:id>', login_required(views.edit_project), name='editProject'),
]
