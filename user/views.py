from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView, CreateView, DeleteView
from django.urls import reverse_lazy

from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


def account_details(request):
    user = CustomUser.objects.get(username=request.user)
    context = {'user': user}
    return render(request, 'user/account.html', context)


class LoginView(LoginView):
    template_name = "user/login.html"


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "user/signup.html"


class AccountDelete(DeleteView):
    model = CustomUser
    context_object_name = 'CustomUser'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        return super(AccountDelete, self).form_valid(form)


def edit_account(request, id):
    post = get_object_or_404(CustomUser, id=id)

    if request.method == 'GET':
        context = {'form': CustomUserChangeForm(instance=post), 'id': id}
        return render(request, 'user/account_edit.html', context)
    elif request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('account')
        else:
            return render(request, 'user/account_edit.html', {'form': form})
