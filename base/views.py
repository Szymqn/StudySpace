from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView

from user.models import CustomUser
from .models import Project, Topic
from .forms import ProjectForm, TopicForm

# Create your views here.


def home(request):
    return render(request, 'base/home.html')


def aboutUs(request):
    return render(request, 'base/about_us.html')


def leaderboard(request):
    users = CustomUser.objects.order_by('-score')
    return render(request, 'base/leaderboard.html', {'users': users})


def projects(request):
    projects_query = Project.objects.all()
    context = {'projects': projects_query}
    return render(request, 'base/projects.html', context)


def topics(request):
    topics_query = Topic.objects.all()
    context = {'topics': topics_query}
    return render(request, 'base/topics.html', context)


def create_topic(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.author = request.user
            form.save()
            return redirect('topics')
    else:
        form = TopicForm()

    return render(request, 'base/create_topic.html', {'form': form})


def addTopic(request):
    return render(request, 'user/add_topic.html')


def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.author = request.user
            form.save()
            return redirect('projects')
    else:
        form = ProjectForm()

    return render(request, 'base/create_project.html', {'form': form})
