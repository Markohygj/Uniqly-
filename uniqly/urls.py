from django.urls import path
from uniqly.views import PostListView,PostCreateView,MassageCreateViews

urlpatterns = [
    path("", PostListView.as_view(), name="post"),
    path("new_post/", PostCreateView.as_view(), name="new_post"),
    path("massages/", MassageCreateViews.as_view(), name="massages")
    ]