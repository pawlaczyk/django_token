from django.contrib import admin
from .models import Book

# admin.site.register(Book)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    Inny sposób rejestracji widoków dla admina
    """
    fields = ['title', 'description', 'is_published'] #można decydowac które pola są widoczne u admina
    list_display =  ['title', 'price']
    list_filter = ['published']
    search_fields = ['title', 'description']