from django.db import models
# from book.models import Book

class Author(models.Model):
    name = models.CharField(max_length=255)
    biography = models.TextField(max_length=999)
    # books = models.ForeignKey(Book, related_name='books', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'