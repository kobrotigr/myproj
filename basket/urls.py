from django.urls import path
from .views import BasketList, add_to_basket


urlpatterns = [
    path('', BasketList.as_view(), name='basket'),
    path('add', add_to_basket, name = 'add'),
]
