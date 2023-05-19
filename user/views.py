from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.views.generic import FormView, CreateView
from django.urls import reverse_lazy


def account(request):
    return render(request, 'user/account.html')


class Register(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'user/register.html'
