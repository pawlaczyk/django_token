from django.contrib import admin
from .models import Book, BookNumber, Character

# admin.site.register(Book)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    Inny sposób rejestracji widoków dla admina
    """
    fields = ['title', 'description', 'is_published', 'isbn'] #można decydowac które pola są widoczne u admina
    list_display =  ['title', 'price']
    list_filter = ['published']
    search_fields = ['title', 'description']


admin.site.register(BookNumber)
admin.site.register(Character)
