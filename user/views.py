from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, ListView
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


class ProfileView(LoginRequiredMixin, CreateView, ListView):
    template_name = 'user/profile.html'
    form_class = AddressForm
    success_url = "/user/profile/"
    login_url = "/user/login/"

    def get_queryset(self):
        return self.request.user.addresses.all()

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


def custom_logout(request):
    logout(request)
    return redirect("/user/login/")


def deleteAddress(request,address_id):
    if request.user.is_authenticated:
        address_obj = Address.objects.filter(id=address_id, user=request.user)
        if address_obj:
            address_obj.delete()
    return redirect("/user/profile/")