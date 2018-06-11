from django.urls import path
from .views import BookList, BookCreate, BookEdit, BookDetail

urlpatterns = [
    path('', BookList.as_view(), name='shop_list'),
    path('book/new/', BookCreate.as_view(), name='book_new'),
    path('book/edit/<int:pk>/', BookEdit.as_view(), name='book_edit'),
    path('book/<int:pk>/', BookDetail.as_view(), name='book_detail'),
]
