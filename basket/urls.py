from django.urls import path
from .views import BasketList


urlpatterns = [
    path('', BasketList.as_view(), name='basket'),
]
