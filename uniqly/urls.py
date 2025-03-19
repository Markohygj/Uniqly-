from django.urls import path
from uniqly.views import PostListView,PostCreateView,MassageCreateViews,ExploreListView,NotificationsListView,MoreListView

urlpatterns = [
    path("", PostListView.as_view(), name="post"),
    path("new_post/", PostCreateView.as_view(), name="new_post"),
    path("massages/", MassageCreateViews.as_view(), name="massages"),
    path("explore/", ExploreListView.as_view(), name="explore"),
    path("notifications/", ExploreListView.as_view(), name="notifications"),
    path("more/", MoreListView.as_view(), name="more")
    ]