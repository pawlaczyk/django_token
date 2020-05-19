from rest_framework import serializers

from .models import Author, Book, BookNumber, Character


class BookNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookNumber
        fields = ['id', 'isbn_10', 'isbn_13']


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['id', 'name', 'surname']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'surname']


class BookSerializer(serializers.ModelSerializer):
    isbn = BookNumberSerializer(many=False) #one to one
    characters = CharacterSerializer(many=True) # one to many
    authors = AuthorSerializer(many=True) #many To many

    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'price', 'published', 'is_published', 'isbn', 'characters', 'authors']


class BookMiniSerializer(serializers.ModelSerializer):
    """
    #optymalizacja query do bazy
    """
    class Meta:
        model = Book
        fields = ['id', 'title']