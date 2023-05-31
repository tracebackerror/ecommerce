from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from .forms import *
from django.shortcuts import redirect
from django.contrib.auth import logout


class CustomLoginView(LoginView):
    template_name = 'user/login.html'
    form_class = CustomLoginForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("/")
        return super().get(request, *args, **kwargs)
    


class CustomRegistrationView(CreateView):
    template_name = 'user/registration.html'
    form_class = CustomRegistrationForm
    success_url = "/user/login/"



def custom_logout(request):
    logout(request)
    return redirect("/user/login/")
