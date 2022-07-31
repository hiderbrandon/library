from curses import meta
from sys import path_hooks
from django import urls
from django.urls import URLPattern, path
from .views import BookAPIView 

urlpatterns = [
    path("", BookAPIView.as_view(), name="book_list"),
    
]

