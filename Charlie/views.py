from django.shortcuts import render
from .models import Book
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .serilizer import bookSerializer

# Create your views here.


class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = bookSerializer


class BookdetailView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = bookSerializer


class BookCreateView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = bookSerializer


class BookUpdateView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = bookSerializer


class BookDeleteView(DestroyAPIView):
    queryset = Book.objects.all()
