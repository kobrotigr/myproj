from django.shortcuts import redirect, resolve_url
from django.views.generic import ListView
from .models import BasketItem
from django.db import models
from django.views.generic import View
from django.contrib.auth.models import User
from shop.models import Book

class BasketList(ListView):
    model = BasketItem
    context_object_name = 'basket'
    template_name = 'basket/basket_list.html'

    def get_queryset(self):
        return BasketItem.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['price'] = self.get_queryset().aggregate(models.Sum('book__price'))
        return context


def add_to_basket(request):
    if request.method=='POST':
        book_pk = request.POST.get('book_pk', 0)
        try:
            book = Book.objects.get(id=book_pk)
            BasketItem.objects.create(user = request.user, book=book)
        except Book.DoesNotExist:
            pass
        return redirect('shop_list')

def del_from_basket(request):
    if request.method=='POST':
        item_pk = request.POST.get('item_pk', 0)
        try:
            item = BasketItem.objects.get(id=item_pk)
            item.delete()
        except BasketItem.DoesNotExist:
            pass
        return redirect('shop_list')

