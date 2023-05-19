from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView

from . import views


urlpatterns = [
    path('login/', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.Register.as_view(), name='register'),
    path('account/', login_required(views.account), name='account'),
]
