from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4

class User(AbstractUser):
    email = models.EmailField(unique=True)


class Author(models.Model):
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(blank=True, null=False)
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_death = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    LANGUAGE_CHOICES = [
        ('YORUBA', "Y"),
        ('HAUSA', "H"),
        ('IGBO', "I"),
        ('ENGLISH', "E")
    ]

    GENRE_CHOICES = [
        ("FIC", 'FICTION'),
        ("POL", 'POLITICS'),
        ("FIN", 'FINANCE'),
        ("ROM", 'ROMANCE')
    ]

    title = models.CharField(max_length=255, blank=False, null=False)
    isbn = models.CharField(max_length=13, blank=False, null=False)
    description = models.CharField(max_length=255, blank=False, null=False)
    date_added = models.DateTimeField(blank=True, null=True)
    genre = models.CharField(max_length=15, choices=GENRE_CHOICES)
    language = models.CharField(max_length=15, choices=LANGUAGE_CHOICES)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    author = models.ForeignKey('Author', on_delete=models.PROTECT)

    # author = models.ForeignKey('Author', on_delete=models.PROTECT, related_name='book_author')
    def __str__(self):
        return f"{self.title}/n {self.description}/n {self.author} /n {self.genre}"


class BookInstance(models.Model):
    STATUS_CHOICES = [
        ('AVAILABLE', 'A'),
        ('BORROWED', 'B')
    ]

    unique_id = models.UUIDField(primary_key=True, default=uuid4)
    due_back = models.DateField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='A')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.due_back} {self.status} {self.book}"
