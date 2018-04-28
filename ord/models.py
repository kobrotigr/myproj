from django.db import models
from shop.models import Book
from basket.models import BasketItem

# Create your models here.


class OrdItem (models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=70)
    first = models.CharField(max_length=25)
    last = models.CharField(max_length=25)
    phone = models.CharField(max_length=10)
    ord_list = models.ManyToManyField(Book)

    def __str__(self):
        return '%s,%s,%s,%s,%s,%s;'%(self.user,self.first,self.last,self.last,self.phone,self.ord_list)
