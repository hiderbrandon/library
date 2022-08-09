from curses import meta
from sys import path_hooks
from django import urls
from django.urls import URLPattern, path , include
from .views import BookAPIView, DetailBook

urlpatterns = [
    path("", BookAPIView.as_view(), name="book_list" ),
    path("<int:pk>/", DetailBook.as_view(), name="book_detail"),
    path("dj-rest-auth/", include("dj_rest_auth.urls")),

]

