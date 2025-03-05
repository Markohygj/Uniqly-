from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, UserProfileForm, UpdateProfileForm
from django.views.generic import ListView, DetailView
from .models import CustomUser


# Create your views here.
class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'edit_profile.html'
    form_class = UpdateProfileForm
    success_url = reverse_lazy('upd_profile')

    def get_object(self):
        return self.request.user

class ProfileDetailViews(LoginRequiredMixin,DetailView):
    template_name = 'profile.html'
    model = CustomUser
    context_object_name = 'user'


    def get_object(self, queryset=None):
        return self.request.user

