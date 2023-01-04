from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import redirect

from .forms import RegistrationForm, LoginForm


class UserSignUpView(CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy('mainpage')
    template_name = 'users/register.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/')


class UserLoginView(LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/')
