from django.db import models
from django.utils import timezone


class Shop(models.Model):
    User = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    book_author = models.CharField(max_length=50)
    book_title = models.CharField(max_length=200)
    book_price = models.IntegerField()
    book_comment = models.TextField()
    basket = []
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def add_basket(self, book_title, basket):
        basket.append(str(book_title))
        self.published_date = timezone.now()
        self.save()

    def calculate_average_price(self):
        pass

    def __str__(self):
        return self.book_title
