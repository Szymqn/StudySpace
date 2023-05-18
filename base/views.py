from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView


# Create your views here.

def home(request):
    return render(request, 'base/home.html')


def aboutUs(request):
    return render(request, 'base/about_us.html')


def leaderboard(requst):
    return render(requst, 'base/leaderboard.html')


def projects(request):
    return render(request, 'base/projects.html')


def topics(request):
    return render(request, 'base/topics.html')


def addTopic(request):
    return render(request, 'user/add_topic.html')


def addProject(reqeust):
    return render(reqeust, 'user/add_project.html')
