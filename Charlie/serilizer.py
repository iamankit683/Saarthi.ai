from rest_framework import serializers
from .models import Book


class bookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'name', 'isbn', 'authors', 'country',
                  'number_of_pages', 'publisher', 'ReleaseDate')
