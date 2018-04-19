from django.urls import path
from .views import BookList, BookCreate,book_detail

urlpatterns = [
    path('', BookList.as_view(), name='shop_list'),
    path('book/<int:pk>/', book_detail, name='book_detail'),
    path('book/new/', BookCreate.as_view(), name='book_new'),
]
