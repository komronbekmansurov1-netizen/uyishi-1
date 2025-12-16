from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    total_number_of_books = models.IntegerField(default=0)
    nation = models.CharField(max_length=100)
    age = models.BooleanField("Vafot etgan...")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class BookCover(models.TextChoices):
    HARD = 'hard', 'Qattiq jild'
    SOFT = 'soft', 'Yumshoq jild'


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    name = models.CharField(max_length=101)
    pages = models.IntegerField(default=0)
    janri = models.CharField(max_length=101)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cover = models.CharField(
        max_length=10,
        choices=BookCover.choices
    )
    image = models.ImageField(upload_to='books/')
    total_sold = models.IntegerField(default=0)
    in_stock = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Store(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=101)
    list_of_sellings = models.ManyToManyField(Book, blank=True, null=True)
    shop_assistant = models.ForeignKey(User, on_delete=models.CASCADE)
    total_of_sold = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name