from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.views.generic import FormView


def account(request):
    return render(request, 'user/account.html')


class RegisterPage(FormView):
    pass
