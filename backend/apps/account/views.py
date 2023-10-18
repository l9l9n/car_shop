from django.shortcuts import render, redirect, reverse
from django.views.generic import CreateView, FormView
from django.urls import reverse_lazy
from .forms import LoginForm, UserRegisterForm
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect
from django.http import HttpResponse


# Create your views here.

class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm

    def form_valid(self, form):
        data = form.cleaned_data
        username = data['username']
        # email = data['email']
        password = data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return redirect('index')
            else:
                return HttpResponse('Ваш аккаунт неактивен')
        return HttpResponse('Такого юзера не существует')


class UserRegisterView(CreateView):
    template_name = 'register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('index')


def UserLogout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('index')
