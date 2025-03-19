from django.contrib.auth import logout
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, UserProfileForm, UpdateProfileForm
from django.views.generic import ListView, DetailView
from .models import CustomUser
from uniqly.models import Post
from django.shortcuts import redirect
from django.contrib.auth import logout



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
    model = CustomUser, Post
    context_object_name = 'user'
    def get_queryset(self):
        user = self.get_object()
        return Post.objects.filter(author=user).order_by('-created_at')


    def get_object(self, queryset=None):
        return self.request.user

def LogoutView(request):
    logout(request)
    return redirect('home')

class UserListView(ListView):
    model = CustomUser
    template_name = 'Users.html'
    context_object_name = 'users'
    success_url = reverse_lazy("user")

class UserDetailView(DetailView):
    model = CustomUser
    template_name = "user_detail.html"
    context_object_name = 'user'
    succues_url = reverse_lazy("user")