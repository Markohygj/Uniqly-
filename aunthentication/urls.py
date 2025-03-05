
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import RegisterView, ProfileUpdateView,ProfileDetailViews

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),

    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    path('upd_profile/', ProfileUpdateView.as_view(), name='upd_profile'),
    path('profile/', ProfileDetailViews.as_view(), name='profile')


    ]