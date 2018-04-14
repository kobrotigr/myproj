from django.db import models
from shop.models import Book

# Create your models here.

class BasketItem (models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)

    def __str__(self):
        return '{} ({})'.format(self.user.username,self.book.title)
