from django.urls import path
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required

from . import views


urlpatterns = [
    path('login/', views.CustomLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterPage.as_view(), name='register'),
    path('account/', login_required(views.account), name='account'),
]
