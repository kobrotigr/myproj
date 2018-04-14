from django.db import models
from django.utils import timezone


class Book(models.Model):
    User = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    ISBN = models.CharField(max_length=15)
    comment = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def __str__(self):
        return self.title