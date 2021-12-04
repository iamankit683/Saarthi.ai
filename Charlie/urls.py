from django.urls import path
from .views import (BookListView, BookCreateView,
                    BookdetailView, BookUpdateView, BookDeleteView)

urlpatterns = [
    path('booklist/', BookListView.as_view()),
    path('book-create/', BookCreateView.as_view()),
    path('book-detail/<pk>', BookdetailView.as_view()),
    path('book-update/<pk>', BookUpdateView.as_view()),
    path('book-delete/<pk>', BookDeleteView.as_view()),
]
