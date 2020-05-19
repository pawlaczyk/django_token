from .serializers import BookSerializer

from rest_framework import viewsets
from .models import Book


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
