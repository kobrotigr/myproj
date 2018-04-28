from django.db import models
from django.utils import timezone


class Book(models.Model):
    User = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    price = models.FloatField()
    ISBN = models.CharField(max_length=15)
    comment = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title