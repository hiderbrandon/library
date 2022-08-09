from rest_framework import generics
from book.models import Book
from .serializers import BookSerializer


# Create your views here.
class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class DetailBook(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class DetailBook(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
