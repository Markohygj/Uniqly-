from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Post,Massage
from .forms  import PostForm,MassageForm

class PostListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    success_url = reverse_lazy("post")

class PostCreateView(CreateView):
    model = Post
    template_name = "new_post.html"
    form_class = PostForm
    success_url = reverse_lazy("post")

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

class MassageCreateViews(CreateView):
    model = Massage
    form_class = MassageForm
    template_name = "massages.html"

class ExploreListView(ListView):
    model = Post
    template_name = 'explore.html'

class NotificationsListView(ListView):
    model = Post
    template_name = 'notifications.html'

class MoreListView(ListView):
    model = Post
    template_name = 'more.html'

