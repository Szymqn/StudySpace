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


def account(request):
    return render(request, 'user/account.html')


def addTopic(request):
    return render(request, 'user/add_topic.html')


def addProject(reqeust):
    return render(reqeust, 'user/add_project.html')


class CustomLogin(LoginView):
    template_name = 'user/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_succesful_url(self):
        return redirect('home')


class RegisterPage(FormView):
    template_name = 'user/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(RegisterPage, self).get(*args, **kwargs)