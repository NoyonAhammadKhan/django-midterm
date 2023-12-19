from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, DetailView
from .forms import SignUpForm, UserUpdateForm
from django.contrib.auth.models import User
from car_app.models import Order, Car
from django.contrib.auth import authenticate, login, update_session_auth_hash, logout
# Create your views here.


class SignUpView(CreateView):
    model = User
    template_name = 'signup.html'
    success_url = reverse_lazy('login')
    form_class = SignUpForm
    success_message = "Your profile was created successfully"


class UserLogin(LoginView):
    template_name = 'login.html'
    model = User

    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successful')
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy("home")

    def form_invalid(self, form):
        messages.success(self.request, 'Logged in information incorrect')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class UserProfile(DetailView):
    model = User
    pk_url_kwarg = 'id'
    template_name = 'profile.html'

    def post(self, request, *args, **kwargs):
        update_form = UserUpdateForm(data=self.request.POST)
        if update_form.is_valid():
            update_form.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.object
        orders = Order.objects.filter(user=user)
        update_form = UserUpdateForm()
        added_cars = Car.objects.filter(owner=user)
        context['update_form'] = update_form
        context['orders'] = orders
        context['added_cars'] = added_cars
        context['user_info'] = user
        return context


def user_logout(request):
    logout(request)
    return redirect('login')
