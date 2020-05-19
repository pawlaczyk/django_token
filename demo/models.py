from django.db import models


class BookNumber(models.Model):
    """
    unique ISBN number
    One to One
    1 -book
    1 - isbn
    """
    isbn_10 = models.CharField(max_length=10, blank=True)
    isbn_13 = models.CharField(max_length=13, blank=True)


class Book(models.Model): # glowna tabela
    title = models.CharField(max_length=36, blank=False, unique=True)
    description = models.TextField(max_length=256, blank=True)
    price = models.DecimalField(default=0, max_digits=3, decimal_places=2)
    published = models.DateField(blank=True, null=True, default=None)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='covers/', blank=True)

    isbn = models.OneToOneField(BookNumber, null=True,
                                blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Character(models.Model):
    """One to many
    1 - book
    N - character"""
    name = models.CharField(max_length=36)
    surname = models.CharField(max_length=36)
    book = models.ForeignKey(Book, on_delete=models.CASCADE,
                             related_name='characters') #referencja na glowna tabele