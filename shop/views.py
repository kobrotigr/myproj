from django.shortcuts import render


# Create your views here.
from .models import Book
from django.views.generic import ListView


class BookList(ListView):
    model = Book
    template_name = 'shop/shop_list.html'
    queryset = Book.objects.all()
    context_object_name = 'books'

