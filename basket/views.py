from django.views.generic import ListView
from .models import BasketItem
from django.db import models


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