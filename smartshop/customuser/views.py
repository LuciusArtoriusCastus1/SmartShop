from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from customuser.forms import SignUpUserForm, SignInUserForm, UpdateUserForm
from customuser.models import User


from django.contrib.auth.mixins import LoginRequiredMixin


class SignUpUserView(CreateView):
    model = User
    form_class = SignUpUserForm
    template_name = 'customuser/signup.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


class SignInUserView(LoginView):
    model = User
    form_class = SignInUserForm
    template_name = 'customuser/login.html'

    def get_success_url(self):
        return reverse_lazy('index')


def log_out(request):
    logout(request)

    return redirect('index')


class UpgradeToSeller(UpdateView, LoginRequiredMixin):
    model = User
    form_class = UpdateUserForm
    template_name = 'customuser/upgrade_user.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.seller_status = True
        user.save()
        return redirect('index')

