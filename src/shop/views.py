# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView

from basket.models import BasketItem
from .forms import ShopForm
from .models import Book
from django.shortcuts import redirect, render


class BookList(ListView):
    model = Book
    template_name = 'shop/shop_list.html'
    queryset = Book.objects.all()
    context_object_name = 'books'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['basket_items'] = BasketItem.objects.filter(user=self.request.user)
        return context

class BookCreate(LoginRequiredMixin,CreateView):
    model = Book
    template_name = 'shop/book_edit.html'
    form_class = ShopForm

    def get_success_url(self):
        return reverse('shop_list')

    def form_valid(self, form):
        form.instance.User = self.request.user
        form.save(True)
        return super(BookCreate, self).form_valid(form)

class BookEdit(LoginRequiredMixin, UpdateView):
    model = Book
    template_name = 'shop/book_edit.html'
    form_class = ShopForm

    def get_success_url(self):
        return reverse('shop_list')


class BookDetail(DetailView):
    model = Book
    template_name = 'shop/book_detail.html'
