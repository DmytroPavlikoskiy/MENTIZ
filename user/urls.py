from django.urls import include, path

from .views import UserProfileListView, UserCreate

urlpatterns = [
    path("user/", UserCreate.as_view(), name="user"),
    path("all-profiles/", UserProfileListView.as_view(), name="all-profiles"),
]